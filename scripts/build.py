#!/usr/bin/env python3
"""Build deterministic static HEA files; no runtime dependencies or network calls."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path
from validate import ROOT, load_data, validate


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')


def build(root=ROOT, output=None):
    root = Path(root).resolve()
    output = Path(output).resolve() if output else root / 'dist'
    if output == root or output in root.parents or (root in output.parents and output != root / 'dist'):
        raise ValueError('Output must not be the project directory or its ancestor')
    data = load_data(root)
    errors = validate(data)
    if errors:
        raise ValueError('\n'.join(errors))
    if not (root / 'web' / 'index.html').is_file():
        raise ValueError('web/index.html is required')
    # Only replace the dedicated output directory after source validation succeeds.
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(root / 'web', output)
    target = output / 'data'
    target.mkdir(exist_ok=True)
    for name, value in data.items():
        (target / f'{name}.json').write_bytes(encoded(value))
    digest = hashlib.sha256(encoded(data)).hexdigest()
    manifest = {
        'schema_version': '1.0.0', 'dataset_version': '0.1.0',
        'language': 'en', 'license': 'CC0-1.0',
        'content_sha256': digest,
        'counts': {name: len(value) for name, value in data.items()},
        'files': {name: f'{name}.json' for name in data},
        'atlas': 'atlas.json',
    }
    (target / 'manifest.json').write_bytes(encoded(manifest))
    (target / 'atlas.json').write_bytes(encoded({'manifest': manifest, **data}))
    (output / '.nojekyll').touch()
    for name in ('README.md', 'LICENSE', 'AGENTS.md', 'CLAUDE.md', 'CONTRIBUTING.md', 'MILESTONES.md', 'llms.txt'):
        if (root / name).is_file():
            shutil.copy2(root / name, output / name)
    if (root / 'docs').is_dir():
        shutil.copytree(root / 'docs', output / 'docs', dirs_exist_ok=True)
    if (root / 'schema').is_dir():
        shutil.copytree(root / 'schema', output / 'schema', dirs_exist_ok=True)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        manifest = build(args.root, args.output)
    except (OSError, ValueError) as exc:
        print(str(exc))
        return 1
    print('Built dist: ' + ', '.join(f'{n} {name}' for name, n in manifest['counts'].items()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
