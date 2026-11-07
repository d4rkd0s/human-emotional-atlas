import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate import validate, load_data
from build import build


def fixture():
    source = dict(id='source', title='Test source', url='https://example.org/source', tradition='test', scope='fixture only', limitations='not real evidence')
    a = dict(id='a', name='A', kind='emotion', definition='Fixture state A.', aliases=[], components=[], qualities=dict(valence='variable', arousal='variable', intensity='variable', time_course='variable'), body=[], thoughts=[], action_tendencies=[], needs=[], contexts=[], examples=[dict(text='Fixture.', possible_states=['a', 'b'], note='Synthetic.')], source_ids=['source'], notes='Fixture only.')
    b = copy.deepcopy(a); b.update(id='b', name='B')
    edge = dict(id='a-b', **{'from':'a', 'to':'b'}, type='neighbor', description='Fixture relationship.', conditions=[], counterexamples=[], source_ids=['source'], basis='editorial_synthesis')
    return dict(states=[a,b], relations=[edge], sources=[source])


class ValidationTests(unittest.TestCase):
    def test_good_and_empty(self):
        self.assertEqual(validate(fixture()), [])
        self.assertEqual(validate(dict(states=[], relations=[], sources=[])), [])

    def test_rejects_dangling_references(self):
        data=fixture(); data['relations'][0]['to']='missing'
        self.assertTrue(any('unknown state reference' in e for e in validate(data)))
        data=fixture(); data['states'][0]['source_ids']=['missing']
        self.assertTrue(any('unknown sources reference' in e for e in validate(data)))

    def test_rejects_duplicate_ids_and_semantic_edges(self):
        data=fixture(); data['states'].append(copy.deepcopy(data['states'][0]))
        self.assertTrue(any('duplicate a' in e for e in validate(data)))
        data=fixture(); edge=copy.deepcopy(data['relations'][0]); edge.update(id='b-a', **{'from':'b','to':'a'});data['relations'].append(edge)
        self.assertTrue(any('duplicate semantic edge' in e for e in validate(data)))

    def test_rejects_recursive_components(self):
        data=fixture(); data['states'][0]['components']=['b'];data['states'][1]['components']=['a']
        self.assertTrue(any('cycle detected' in e for e in validate(data)))

    def test_rejects_private_scores_deeply(self):
        data=fixture(); data['states'][0]['examples'][0]['confidence_score']=0.9
        self.assertTrue(any('must remain private' in e for e in validate(data)))

    def test_malformed_values_report_errors_without_crashing(self):
        for field in ('kind','components','qualities','examples','aliases','source_ids'):
            data=fixture(); data['states'][0][field]=None
            self.assertTrue(validate(data),field)
        for field in ('type','basis','from','to'):
            data=fixture();data['relations'][0][field]=[]
            self.assertTrue(validate(data),field)

    def test_missing_source_and_self_edge(self):
        data=fixture();data['relations'][0]['source_ids']=[];data['relations'][0]['to']='a'
        errors=validate(data)
        self.assertTrue(any('at least one source' in e for e in errors))
        self.assertTrue(any('self relation' in e for e in errors))

    def test_partial_missing_files_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'data').mkdir();(root/'data/states.json').write_text('[]')
            with self.assertRaises(FileNotFoundError):load_data(root)

    def test_deterministic_build_and_invalid_data_does_not_destroy_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'data').mkdir();(root/'web').mkdir();(root/'web/index.html').write_text('<title>HEA</title>')
            for key,value in fixture().items():(root/'data'/f'{key}.json').write_text(json.dumps(value))
            build(root)
            before={p.relative_to(root/'dist'):p.read_bytes() for p in (root/'dist').rglob('*') if p.is_file()}
            build(root)
            after={p.relative_to(root/'dist'):p.read_bytes() for p in (root/'dist').rglob('*') if p.is_file()}
            self.assertEqual(before,after)
            (root/'data/states.json').write_text('[{}]')
            with self.assertRaises(ValueError):build(root)
            self.assertEqual((root/'dist/data/states.json').read_bytes(),before[Path('data/states.json')])

    def test_build_refuses_source_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            with self.assertRaises(ValueError):build(root,root/'data')

if __name__ == '__main__':
    unittest.main()
