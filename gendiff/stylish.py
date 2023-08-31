import json
INDENT = '  '
STATUS = {'unchanged': ' ',
          'added': '+',
          'deleted': '-'}


def convert_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value


def convert_to_string(value, depth=1):
    result_lst = ["{"]
    if not isinstance(value, dict):
        return convert_value(value)
    elif isinstance(value, dict):
        for key, val in value.items():
            val = convert_value(val)
            result_lst.append(f" {INDENT * depth} {key}: {convert_to_string(val, depth+2)}")
        result_lst.append(f"{INDENT * (depth-1)}}}")
    return '\n'.join(result_lst)


def convert_to_format_stylish(diff, depth=1):
    result_diff = []
    for key, status in diff.items():
        type_ = status.get('type')
        value = status.get('value')
        if type_ == 'nested':
            result_diff.append(f"{INDENT * depth}  {key}: {{\n"
                               f"{convert_to_format_stylish(value, depth+2)}")
            result_diff.append(f"{INDENT * (depth + 1)}}}\n")
        elif type_ == 'changed':
            old_value = value.get('old value')
            new_value = value.get('new value')
            result_diff.append(f"{INDENT * depth}- {key}: "
                               f"{convert_to_string(old_value, depth+2)}\n")
            result_diff.append(f"{INDENT * depth}+ {key}: "
                               f"{convert_to_string(new_value, depth+2)}\n")
        else:
            result_diff.append(f"{INDENT * depth}{STATUS[type_]} {key}: "
                               f"{convert_to_string(value, depth+2)}\n")
    result_diff = ''.join(result_diff)
    return result_diff
