from typing import Any


OUTPUT_TEMPLATE = {
    'ADDED': "Property '{0}' was added with value: {1}",
    'REMOVED': "Property '{0}' was removed",
    'CHANGED': "Property '{0}' was updated. From {1} to {2}",
    'COMPLEX': "[complex value]",
}


def render(tree: dict, parent: str = '') -> str:
    result_array = []

    for item_, values in tree.items():
        item = get_property(parent, item_)
        if values['type'] == 'ADDED':
            element = OUTPUT_TEMPLATE['ADDED'].format(
                item,
                get_value(values['value']))
        if values['type'] == 'REMOVED':
            element = OUTPUT_TEMPLATE['REMOVED'].format(
                item,
                get_value(values['value']))
        if values['type'] == 'CHANGED':
            element = OUTPUT_TEMPLATE['CHANGED'].format(
                item,
                get_value(values['old_value']),
                get_value(values['new_value']))
        elif values['type'] == 'NESTED':
            element = render(values['value'], item)

        result_array.append(element)

    result = sorted(list(set(result_array)))

    return '\n'.join(result)


def get_property(parent: str, item: Any) -> str:
    if not parent:
        return item
    return f'{parent}.{item}'


def get_value(element: Any) -> str:
    if isinstance(element, dict):
        return OUTPUT_TEMPLATE['COMPLEX']
    elif element == 'true':
        return 'true'
    elif element == 'false':
        return 'false'
    elif element == 'null':
        return 'null'
    elif isinstance(element, str):
        return f"'{element}'"
    return str(element)
