import json


def convert_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, dict):
        return '[complex value]'
    return value


def make_path(key, route):
    if len(route) > 1:
        return route + f'.{key}'
    return f'{key}'


def get_format_plain(diff, route=''):
    result_property = []
    for key, value in diff.items():
        path = make_path(key, route)
        types = value.get('type')
        values = value.get('value')
        if types == 'nested':
            result_property.append(get_format_plain(values, path))
        elif types == 'changed':
            old_value = values.get('old value')
            new_value = values.get('new value')
            result_property.append(f"Property '{path}' was updated. "
                                   f"From {convert_value(old_value)} "
                                   f"to {convert_value(new_value)}")
        elif types == 'added':
            result_property.append(f"Property '{path}' was added "
                                   f"with value: {convert_value(values)}")
        elif types == 'deleted':
            result_property.append(f"Property '{path}' was removed")
    result_property = '\n'.join(result_property)
    return result_property
