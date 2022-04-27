from gendiff.lib.input_parser import open_files
from gendiff.lib.diff import calculate_differences
from gendiff.lib.formaters import stylish, plain


def generate_diff(file_path1: str, file_path2: str, format='stylish'):
    source1 = open_files(file_path1)
    source2 = open_files(file_path2)
    if format == 'stylish':
        return stylish.render(calculate_differences(source1, source2))
    elif format == 'plain':
        return plain.render(calculate_differences(source1, source2))
