from gendiff.lib.diff import open_files, calculate_differences
from gendiff.lib.format import render


def generate_diff(file_path1: str, file_path2: str):
    source1 = open_files(file_path1)
    source2 = open_files(file_path2)
    return render(calculate_differences(source1, source2))
