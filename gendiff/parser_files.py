import json
import yaml
from pathlib import Path


def open_files(path):
    ext = Path(path).suffix
    if ext == '.json':
        content = json.load(open(path))
        return content
    elif ext == '.yml' or ext == '.yaml':
        content = yaml.load(open(path), Loader=yaml.BaseLoader)
        return content
    else:
        return "Wrong file format"


def calculate_differences(source1, source2) -> str:
    """Вычислитий отличий плоскиx файлов"""
    keys = sorted(list(set(source1.keys()) | set(source2.keys())))
    differences = []
    for key in keys:
        if key in source1 and not(key in source2):
            differences.append(f" - {key}: {bool_to_str(source1[key])}")

        if not(key in source1) and key in source2:
            differences.append(f" + {key}: {bool_to_str(source2[key])}")

        if key in source1 and key in source2:
            if source1[key] == source2[key]:
                differences.append(f"   {key}: {bool_to_str(source1[key])}")
            else:
                differences.append(f" - {key}: {bool_to_str(source1[key])}")
                differences.append(f" + {key}: {bool_to_str(source2[key])}")
    

def formater(difference):
    result = '{'
    for value in difference:
        result = '\n'.join([result, value.lower()])
    result = '\n'.join([result, '}'])
    return result


def bool_to_str(temp) -> str:
    if type(temp) == bool:
        return str(temp).lower()
    return temp
