# flake8: noqa
import yaml
import json

from gendiff import generate_diff
from gendiff.lib.formaters import plain, stylish, my_json
from gendiff.lib.input_data import get_data, _open_files
from gendiff.lib.diff import calculate_differences
FILE_PLAIN_JSON_1 = 'tests/fixtures/plain/file1.json'
FILE_PLAIN_JSON_2 = 'tests/fixtures/plain/file2.json'
FILE_PLAIN_YAML_1 = 'tests/fixtures/plain/file1.yml'
FILE_PLAIN_YAML_2 = 'tests/fixtures/plain/file2.yml'

FILE_STAYLISH_JSON_1 = 'tests/fixtures/stylish/file1.json'
FILE_STAYLISH_JSON_2 = 'tests/fixtures/stylish/file2.json'
FILE_STAYLISH_YAML_1 = 'tests/fixtures/stylish/file1.yml'
FILE_STAYLISH_YAML_2 = 'tests/fixtures/stylish/file2.yml'

TEST_PLAIN_JSON = 'tests/fixtures/plain/test_json.txt'
TEST_PLAIN_YAML = 'tests/fixtures/plain/test_yaml.txt'
TEST_STAYLISH_JSON = 'tests/fixtures/stylish/test_json.txt'
TEST_STAYLISH_YAML = 'tests/fixtures/stylish/test_yaml.txt'

TEST_RENDER_STAYLISH = 'tests/fixtures/render/test_stylish.txt'
TEST_RENDER_PLAIN = 'tests/fixtures/render/test_plain.txt'
TEST_RENDER_JSON = 'tests/fixtures/render/test_json.txt'


def open_correct_answer(file_name):
    f = open(file_name)
    correct_answer = f.read()
    f.close()
    return correct_answer


def test_open_files_json():
    with open(FILE_PLAIN_JSON_1) as file:
        correct_answer = json.load(file) 
    assert correct_answer == _open_files(FILE_PLAIN_JSON_1)


def test_open_files_yaml():
    with open(FILE_PLAIN_YAML_1) as file:
        correct_answer = yaml.load(file, Loader=yaml.BaseLoader)
    assert  correct_answer == _open_files(FILE_PLAIN_YAML_1)


def test_open_files_wrong():
    assert _open_files(TEST_PLAIN_JSON) == "Wrong file format"


def test_calculate_differences_plain_json():
    source1 = get_data(FILE_PLAIN_JSON_1)
    source2 = get_data(FILE_PLAIN_JSON_2)
    correct_answer = open_correct_answer(TEST_PLAIN_JSON)
    assert correct_answer == str(calculate_differences(source1, source2))


def test_calculate_differences_plain_yaml():
    source1 = get_data(FILE_PLAIN_YAML_1)
    source2 = get_data(FILE_PLAIN_YAML_2)
    correct_answer = open_correct_answer(TEST_PLAIN_YAML)
    assert correct_answer == str(calculate_differences(source1, source2))


def test_calculate_differences_stylish_json():
    source1 = get_data(FILE_STAYLISH_JSON_1)
    source2 = get_data(FILE_STAYLISH_JSON_2)
    correct_answer = open_correct_answer(TEST_STAYLISH_JSON)
    assert correct_answer == str(calculate_differences(source1, source2))


def test_calculate_differences_stylish_yaml():
    source1 = get_data(FILE_STAYLISH_YAML_1)
    source2 = get_data(FILE_STAYLISH_YAML_2)
    correct_answer = open_correct_answer(TEST_STAYLISH_YAML)
    assert correct_answer == str(calculate_differences(source1, source2))


def test_render_stylish():
    source1 = get_data(FILE_STAYLISH_JSON_1)
    source2 = get_data(FILE_STAYLISH_JSON_2)
    content = calculate_differences(source1, source2)
    correct_answer = open_correct_answer(TEST_RENDER_STAYLISH)
    assert correct_answer == str(stylish.render(content))


def test_render_plain():
    source1 = get_data(FILE_STAYLISH_JSON_1)
    source2 = get_data(FILE_STAYLISH_JSON_2)
    content = calculate_differences(source1, source2)
    correct_answer = open_correct_answer(TEST_RENDER_PLAIN)
    assert correct_answer == str(plain.render(content))


def test_render_json():
    source1 = get_data(FILE_STAYLISH_JSON_1)
    source2 = get_data(FILE_STAYLISH_JSON_2)
    content = calculate_differences(source1, source2)
    correct_answer = open_correct_answer(TEST_RENDER_JSON)
    assert correct_answer == str(my_json.render(content))


def test_generate_diff_stylish():
    correct_answer = open_correct_answer(TEST_RENDER_STAYLISH)
    assert correct_answer == str(generate_diff(FILE_STAYLISH_JSON_1, FILE_STAYLISH_JSON_2))


def test_generate_diff_plain():
    correct_answer = open_correct_answer(TEST_RENDER_PLAIN)
    assert correct_answer == str(generate_diff(FILE_STAYLISH_JSON_1, FILE_STAYLISH_JSON_2, 'plain'))


def test_generate_diff_json():
    correct_answer = open_correct_answer(TEST_RENDER_JSON)
    assert correct_answer == str(generate_diff(FILE_STAYLISH_JSON_1, FILE_STAYLISH_JSON_2, 'json'))