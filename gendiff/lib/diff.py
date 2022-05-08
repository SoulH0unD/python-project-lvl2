from typing import Any


def calculate_differences(source1: dict, source2: dict) -> dict:
    """Вычислитель отличий"""
    keys = list(source1.keys() | source2.keys())
    return {key: gen_tree_diff(key, source1, source2) for key in sorted(keys)}


def gen_tree_diff(key: Any, first: Any, second: Any) -> dict:
    """Генерация дерева различий"""
    first_value = check_value(key, first)
    second_value = check_value(key, second)
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


def check_value(k, v):
    if k in v:
        if v[k] is None:
            return 'null'
        elif isinstance(v[k], (int, float)):
            return v[k]
        elif v[k] == True:
            return 'true'
        elif v[k] == False:
            return 'false'
        else:
            return v[k]
    else:
        return None
