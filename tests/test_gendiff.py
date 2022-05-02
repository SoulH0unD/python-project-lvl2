import yaml
import json
from gendiff.lib.input_parser import open_files
from gendiff.lib.diff import calculate_differences

def test_open_files():
    assert open_files('tests/fixtures/file1.yml') == yaml.load(open('tests/fixtures/file1.yml'), Loader=yaml.BaseLoader)
    assert open_files('tests/fixtures/file1.json') == json.load(open('tests/fixtures/file1.json'))
    assert open_files('tests/fixtures/test_files.txt') == "Wrong file format"


def test_calculate_differences():
    source1 = open_files('tests/fixtures/file1.json')
    source2 = open_files('tests/fixtures/file2.json')
    test_str = "{'follow': {'type': 'REMOVED', 'value': False}, 'host': {'type': 'EQUALS', 'value': 'hexlet.io'}, 'proxy': {'type': 'REMOVED', 'value': '123.234.53.22'}, 'timeout': {'type': 'CHANGED', 'old_value': 50, 'new_value': 20}, 'verbose': {'type': 'ADDED', 'value': True}}"
    assert test_str == str(calculate_differences(source1, source2))