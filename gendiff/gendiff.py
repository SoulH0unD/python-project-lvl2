from gendiff.lib.input_data import get_data
from gendiff.lib.diff import calculate_differences
from gendiff.lib.formaters import my_json, stylish, plain


def generate_diff(file_path1: str,
                  file_path2: str,
                  format_name: str = 'stylish') -> str:
    source1 = get_data(file_path1)
    source2 = get_data(file_path2)
    if format_name == 'stylish':
        return stylish.render(calculate_differences(source1, source2))
    elif format_name == 'plain':
        return plain.render(calculate_differences(source1, source2))
    elif format_name == 'json':
        return my_json.render(calculate_differences(source1, source2))
    else:
        return f'{format_name} this format is not supported'
