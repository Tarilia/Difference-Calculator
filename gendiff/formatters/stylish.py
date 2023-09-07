import json
INDENT = '  '
STATUS = {'unchanged': ' ',
          'added': '+',
          'deleted': '-'}


def convert_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value


def make_string(value, depth=1):
    result_lst = ["{"]
    if not isinstance(value, dict):
        return convert_value(value)
    elif isinstance(value, dict):
        for key, val in value.items():
            val = convert_value(val)
            result_lst.append(f" {INDENT * depth} {key}: "
                              f"{make_string(val, depth+2)}")
        result_lst.append(f"{INDENT * (depth-1)}}}")
    return '\n'.join(result_lst)


def get_format_stylish(diff, depth=1):
    result_diff = []
    for key, value in diff.items():
        types = value.get('type')
        values = value.get('value')
        if types == 'nested':
            result_diff.append(f"{INDENT * depth}  {key}: {{\n"
                               f"{get_format_stylish(values, depth+2)}")
            result_diff.append(f"{INDENT * (depth + 1)}}}\n")
        elif types == 'changed':
            old_value = values.get('old value')
            new_value = values.get('new value')
            result_diff.append(f"{INDENT * depth}- {key}: "
                               f"{make_string(old_value, depth+2)}\n")
            result_diff.append(f"{INDENT * depth}+ {key}: "
                               f"{make_string(new_value, depth+2)}\n")
        else:
            result_diff.append(f"{INDENT * depth}{STATUS[types]} {key}: "
                               f"{make_string(values, depth+2)}\n")
    result_diff = ''.join(result_diff)
    return result_diff
