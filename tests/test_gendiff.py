from logging import Formatter
import yaml
import json
from gendiff.lib.formaters import plain, stylish, my_json
from gendiff.lib.input_parser import open_files
from gendiff.lib.diff import calculate_differences
from test_constatn import TEST_PLAIN_JSON, TEST_PLAIN_YAML, TEST_STAYLISH_JSON, TEST_STAYLISH_YAML
from test_constatn import TEST_STAYLISH_RENDER, TEST_PLAIN_RENDER, TEST_JSON_RENDER

def test_open_files():
    assert open_files('tests/fixtures/file1.yml') == yaml.load(open('tests/fixtures/file1.yml'), Loader=yaml.BaseLoader)
    assert open_files('tests/fixtures/file1.json') == json.load(open('tests/fixtures/file1.json'))
    assert open_files('tests/fixtures/test_files.txt') == "Wrong file format"


def test_calculate_differences():
    #Сравнение плоских файлов(json)
    source1 = open_files('tests/fixtures/file1.json')
    source2 = open_files('tests/fixtures/file2.json')
    assert TEST_PLAIN_JSON == str(calculate_differences(source1, source2))
    #Сравнение плоских файлов(yaml)
    source1 = open_files('tests/fixtures/file1.yml')
    source2 = open_files('tests/fixtures/file2.yml')
    assert TEST_PLAIN_YAML == str(calculate_differences(source1, source2))
    #Сравнение вложенных структур(json)
    source1 = open_files('tests/fixtures/stylish/file1.json')
    source2 = open_files('tests/fixtures/stylish/file2.json')
    assert TEST_STAYLISH_JSON == str(calculate_differences(source1, source2))
    #Сравнение вложенных структур(yaml)
    source1 = open_files('tests/fixtures/stylish/file1.yml')
    source2 = open_files('tests/fixtures/stylish/file2.yml')
    assert TEST_STAYLISH_YAML == str(calculate_differences(source1, source2))

def test_render():
    source1 = open_files('tests/fixtures/stylish/file1.json')
    source2 = open_files('tests/fixtures/stylish/file2.json')
    content = calculate_differences(source1, source2)
    assert TEST_STAYLISH_RENDER == stylish.render(content)
    assert TEST_PLAIN_RENDER == plain.render(content)
    assert TEST_JSON_RENDER == my_json.render(content)