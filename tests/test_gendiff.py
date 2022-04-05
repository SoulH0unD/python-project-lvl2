from gendiff import generate_diff


def test_generate_diff():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    res = ''
    with open('tests/fixtures/test_file1_2.txt') as txt_diff:
        res = txt_diff.read()

    res = '{\n' + res + '\n}'
    assert result == res