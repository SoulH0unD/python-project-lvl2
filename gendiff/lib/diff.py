def calculate_differences(source1, source2):
    keys = list(source1.keys() | source2.keys())
    return {key: gen_tree_diff(key, source1, source2) for key in sorted(keys)}


def gen_tree_diff(key, first, second):
    first_value = first.get(key)
    second_value = second.get(key)
    if first_value is None:
        tree = {
            'type': 'ADDED',
            'value': second_value,
        }
    elif second_value is None:
        tree = {
            'type': 'REMOVED',
            'value': first_value,
        }
    elif isinstance(first_value, dict) and isinstance(second_value, dict):
        tree = {
            'type': 'NESTED',
            'value': calculate_differences(first_value, second_value),
        }
    elif first_value == second_value:
        tree = {
            'type': 'EQUALS',
            'value': first_value,
        }
    elif first_value != second_value:
        tree = {
            'type': 'CHANGED',
            'old_value': first_value,
            'new_value': second_value,
        }
    return tree
