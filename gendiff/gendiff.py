import json


def generate_diff(file_path1: str, file_path2: str):#, format_name='stylish') -> str:
    source1 = json.load(open(file_path1))
    source2 = json.load(open(file_path2))
    keys = sorted(
                list(
                    set(source1.keys()) |  set(source2.keys())
                    ))

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
    
    result = '{'
    for value in differences:
        result = result ='\n'.join([result, value.lower()])

    result ='\n'.join([result, '}'])
    return result

def bool_to_str(temp) -> str:
    if type(temp)==bool:
        return str(temp).lower()
    return temp

