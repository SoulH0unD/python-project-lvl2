import yaml
from gendiff.lib.diff import  open_files

def test_open_files():
    assert open_files('tests/fixtures/file1.yml') == yaml.load(open('tests/fixtures/file1.yml'), Loader=yaml.BaseLoader)
