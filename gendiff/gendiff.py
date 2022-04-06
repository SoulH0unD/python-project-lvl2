from gendiff.parser_files import open_files, calculate_differences


def generate_diff(file_path1: str, file_path2: str):
    source1 = open_files(file_path1)
    source2 = open_files(file_path2)

    return calculate_differences(source1, source2)
    
    



