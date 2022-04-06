from importlib.resources import open_binary
import yaml
from gendiff import generate_diff
from gendiff.parser_files import calculate_differences, open_files


def test_generate_diff():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    res = ''
    with open('tests/fixtures/test_file1_2.txt') as txt_diff:
        res = txt_diff.read()
    res = '{\n' + res + '\n}'
    assert result == res


def test_calculate_differences():
    source1 = open_files('tests/fixtures/file1.json')
    source2 = open_files('tests/fixtures/file2.json')
    result =  calculate_differences(source1, source2)
    with open('tests/fixtures/test_file1_2.txt') as txt_diff:
        res = txt_diff.read()
    res = '{\n' + res + '\n}'
    assert result == res


def test_open_files():
    assert open_files('tests/fixtures/file1.yml') == yaml.load(open('tests/fixtures/file1.yml'), Loader=yaml.BaseLoader)
