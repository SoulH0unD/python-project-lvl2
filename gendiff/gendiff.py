import json


def generate_diff(file_path1: str, file_path2: str):#, format_name='stylish'):
    source1 = json.load(open(file_path1))
    source2 = json.load(open(file_path2))
    keys = sorted(
                list(
                    set(source1.keys()) |  set(source2.keys())
                    ))

    differences = []
    for key in keys:
        if key in source1 and not(key in source2):
            differences.append(f"- {key}: {source1[key]}")

        if not(key in source1) and key in source2:
            differences.append(f"+ {key}: {source2[key]}")

        if key in source1 and key in source2:
            if source1[key] == source2[key]:
                differences.append(f"  {key}: {source1[key]}")
            else:
                differences.append(f"- {key}: {source1[key]}")
                differences.append(f"+ {key}: {source2[key]}")


    return differences
    

    #return source1#result
