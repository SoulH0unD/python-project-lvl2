from typing import Any

operator = {
    'ADDED': "{ws}+ {k}: {v}\n",
    'REMOVED': "{ws}- {k}: {v}\n",
    'EQUALS': "{ws}  {k}: {v}\n",
    'CHANGED': "{ws}- {k}: {v1}\n{ws}+ {k}: {v2}\n",
    'NESTED': "  {ws}{k}: {op_br}\n{v}{cl_br}\n"
}


def render(diff: dict) -> str:
    result = do_rendering(diff, indent=2)
    return "{\n" + result + "}"


def do_rendering(tree: dict, indent: int = 1) -> str:
    rendered_lines = []
    ws = ''.rjust(indent)
    for key, value in tree.items():
        state = value['type']
        if state == 'NESTED':
            rend_line = do_rendering(value['value'], indent + 4)
            rend_line = operator[state].format(
                ws=ws,
                k=key,
                op_br='{',
                v=rend_line,
                cl_br='}'.rjust(indent + 3)
            )
        elif state == 'CHANGED':
            before = deploy_dict(value['old_value'], indent)
            after = deploy_dict(value['new_value'], indent)
            rend_line = operator[state].format(
                ws=ws,
                k=key,
                v1=before,
                v2=after
            )
        else:
            new_value = deploy_dict(value['value'], indent)
            rend_line = operator[state].format(ws=ws, k=key, v=new_value)
        rendered_lines.append(rend_line)
    return ''.join(rendered_lines)


def deploy_dict(element: Any, indent: int) -> str:
    if isinstance(element, dict):
        temp = []
        ws = ''.rjust(indent + 6)
        for k, v in element.items():
            val = deploy_dict(v, indent + 4)
            line = f'{ws}{k}: {val}\n'
            temp.append(line)
        return "{\n" + ''.join(temp) + "}".rjust(indent + 3)
    return element
