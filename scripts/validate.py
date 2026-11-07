#!/usr/bin/env python3
"""Validate HEA structure and graph integrity using only Python's standard library."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
KINDS = {'emotion', 'mood', 'quality', 'mixed_state', 'mental_state'}
RELATIONS = {'neighbor', 'contrast', 'may_transition_to', 'may_cooccur', 'component_of'}
BASES = {'empirical', 'tradition_specific', 'editorial_synthesis'}
PRIVATE_KEYS = {'confidence', 'confidence_score', 'confidence_scores', 'probability', 'probabilities', 'statistics', 'p_value', 'review_score'}


def load_data(root=ROOT):
    paths = [Path(root) / 'data' / f'{name}.json' for name in ('states', 'relations', 'sources')]
    if not any(path.exists() for path in paths):
        return {'states': [], 'relations': [], 'sources': []}
    return {path.stem: json.loads(path.read_text(encoding='utf-8')) for path in paths}


def validate(data):
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)
    def text(value):
        return isinstance(value, str) and bool(value.strip())
    def strings(value):
        return isinstance(value, list) and all(text(v) for v in value)
    def private(value, path):
        if isinstance(value, dict):
            for key, child in value.items():
                check(key.lower() not in PRIVATE_KEYS, f'{path}.{key}: builder scores/statistics must remain private')
                private(child, f'{path}.{key}')
        elif isinstance(value, list):
            for index, child in enumerate(value):
                private(child, f'{path}[{index}]')
    private(data, 'data')
    tables = {}
    for name in ('states', 'relations', 'sources'):
        rows = data.get(name)
        check(isinstance(rows, list), f'{name}: expected array')
        tables[name] = rows if isinstance(rows, list) else []
    ids = {}
    for name, rows in tables.items():
        ids[name] = set()
        for index, row in enumerate(rows):
            path = f'{name}[{index}]'
            check(isinstance(row, dict), f'{path}: expected object')
            if not isinstance(row, dict):
                continue
            identifier = row.get('id')
            if not isinstance(identifier, str) or not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', identifier):
                errors.append(f'{path}.id: expected lowercase kebab-case identifier')
                continue
            check(identifier not in ids[name], f'{path}.id: duplicate {identifier}')
            ids[name].add(identifier)
    def references(values, target, path, nonempty=False):
        check(strings(values), f'{path}: expected string array')
        if isinstance(values, list):
            check(not nonempty or bool(values), f'{path}: at least one source required')
            check(len(values) == len(set(v for v in values if isinstance(v, str))), f'{path}: duplicate or malformed references')
            for value in values:
                check(isinstance(value, str) and value in ids[target], f'{path}: unknown {target} reference {value!r}')
    for row in tables['sources']:
        if not isinstance(row, dict):
            continue
        path = f'sources/{row.get("id", "?")}'
        for field in ('title', 'url', 'tradition', 'scope', 'limitations'):
            check(text(row.get(field)), f'{path}.{field}: expected nonempty text')
        url = row.get('url', '')
        parsed = urlparse(url if isinstance(url, str) else '')
        check(parsed.scheme == 'https' and bool(parsed.netloc), f'{path}.url: expected HTTPS URL')
    for row in tables['states']:
        if not isinstance(row, dict):
            continue
        path = f'states/{row.get("id", "?")}'
        for field in ('name', 'definition', 'notes'):
            check(text(row.get(field)), f'{path}.{field}: expected nonempty text')
        check(isinstance(row.get('kind'), str) and row['kind'] in KINDS, f'{path}.kind: unknown kind')
        if 'basis' in row:
            check(isinstance(row['basis'], str) and row['basis'] in BASES, f'{path}.basis: unknown basis')
        for field in ('aliases', 'body', 'thoughts', 'action_tendencies', 'needs', 'contexts'):
            check(strings(row.get(field)), f'{path}.{field}: expected string array')
        references(row.get('components'), 'states', path + '.components')
        check(not isinstance(row.get('components'), list) or row.get('id') not in row['components'], f'{path}.components: cannot contain itself')
        references(row.get('source_ids'), 'sources', path + '.source_ids', True)
        qualities = row.get('qualities')
        check(isinstance(qualities, dict), f'{path}.qualities: expected object')
        if isinstance(qualities, dict):
            for field in ('valence', 'arousal', 'intensity', 'time_course'):
                check(text(qualities.get(field)), f'{path}.qualities.{field}: expected nonempty text')
        examples = row.get('examples')
        check(isinstance(examples, list), f'{path}.examples: expected array')
        if isinstance(examples, list):
            for index, example in enumerate(examples):
                ep = f'{path}.examples[{index}]'
                check(isinstance(example, dict), f'{ep}: expected object')
                if isinstance(example, dict):
                    for field in ('text', 'note'):
                        check(text(example.get(field)), f'{ep}.{field}: expected nonempty text')
                    references(example.get('possible_states'), 'states', ep + '.possible_states')
    seen_edges = set()
    for row in tables['relations']:
        if not isinstance(row, dict):
            continue
        path = f'relations/{row.get("id", "?")}'
        for field in ('from', 'to'):
            value = row.get(field)
            check(isinstance(value, str) and value in ids['states'], f'{path}.{field}: unknown state reference {value!r}')
        check(row.get('from') != row.get('to'), f'{path}: self relation is not allowed')
        check(isinstance(row.get('type'), str) and row['type'] in RELATIONS, f'{path}.type: unknown relation type')
        check(isinstance(row.get('basis'), str) and row['basis'] in BASES, f'{path}.basis: unknown evidence basis')
        check(text(row.get('description')), f'{path}.description: expected nonempty text')
        for field in ('conditions', 'counterexamples'):
            check(strings(row.get(field)), f'{path}.{field}: expected string array')
        references(row.get('source_ids'), 'sources', path + '.source_ids', True)
        if all(isinstance(row.get(k), str) for k in ('from', 'to', 'type')):
            ends = [row['from'], row['to']]
            if row['type'] in {'neighbor', 'contrast', 'may_cooccur'}:
                ends.sort()
            edge = (row['type'], *ends)
            check(edge not in seen_edges, f'{path}: duplicate semantic edge {edge}')
            seen_edges.add(edge)
    # Components form a descriptive acyclic graph, never recursive emotional equations.
    graph = {row['id']: row.get('components', []) for row in tables['states'] if isinstance(row, dict) and isinstance(row.get('id'), str) and isinstance(row.get('components'), list)}
    visiting, done = set(), set()
    def visit(node):
        if node in visiting:
            errors.append(f'states/{node}.components: cycle detected')
            return
        if node in done:
            return
        visiting.add(node)
        for child in graph.get(node, []):
            if isinstance(child, str) and child in graph:
                visit(child)
        visiting.remove(node)
        done.add(node)
    for node in graph:
        visit(node)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        data = load_data(args.root)
        errors = validate(data)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        print('\n'.join(errors))
        return 1
    print('Valid HEA dataset: ' + ', '.join(f'{len(rows)} {name}' for name, rows in data.items()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
