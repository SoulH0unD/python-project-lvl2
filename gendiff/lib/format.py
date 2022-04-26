INTEND = '    '
ADDED = '  + '
REMOVED = '  - ' 


def render(tree, depth=1):
    format = []
    format.append('{')
    intend_ = INTEND * depth
    if depth == 1:
        intend = intend_
        added = ADDED
        removed = REMOVED
    else: 
        intend = intend_ + INTEND
        added = intend_ + ADDED
        removed = intend_ + REMOVED
    for item, values in tree.items():
        if values['type'] == 'ADDED':
            format.append(f'{added}{item}: {deploy_dict(values["value"], intend)}')
        elif values['type'] == 'REMOVED':
            format.append(f'{removed}{item}: {deploy_dict(values["value"], intend)}')
        elif values['type'] == 'EQUALS':
            format.append(f'{intend}{item}: {deploy_dict(values["value"], intend)}')
        elif values['type'] == 'CHANGED':
            format.append(f'{removed}{item}: {deploy_dict(values["old_value"], intend)}')
            format.append(f'{added}{item}: {deploy_dict(values["new_value"], intend)}')
        elif values['type'] == 'NESTED':
            format.append(f'{intend}{item}: {render(values["value"], depth + 1)}')
            format.append(f'{intend}}}')
    return '\n'.join(format) + '\n}' if depth == 1 else '\n'.join(format)


def deploy_dict(element, inten):
    if isinstance(element, dict):
        result = []
        result.append('{')
        for i, v in element.items():
            result.append(f'{INTEND}{inten}{i}: {deploy_dict(v, inten + INTEND)}')
        result.append(f'{inten}}}')
        return '\n'.join(result) 
    return element