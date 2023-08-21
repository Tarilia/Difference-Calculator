import json


ADDED_VALUE = '  + '
REMOTE_VALUE = '  - '
UNCHANGED_VALUE = '    '


def get_string(dictionary):
    result_string = ''
    for key, value in dictionary.items():
        if isinstance(value, bool) or value is None:
            result_string += f'{key}: {json.dumps(value)}\n'
        else:
            result_string += f'{key}: {value}\n'
    return '{\n' + result_string + '}\n'


def generate_diff(path1, path2):
    file1 = json.load(open(path1))
    file2 = json.load(open(path2))
    diff = {}
    shared_keys = sorted(file1.keys() | file2.keys())
    for key in shared_keys:
        if key not in file1 and key in file2:
            diff[f'{ADDED_VALUE}{key}'] = file2[key]
        elif key in file1 and key not in file2:
            diff[f'{REMOTE_VALUE}{key}'] = file1[key]
        elif file1[key] == file2[key]:
            diff[f'{UNCHANGED_VALUE}{key}'] = file2[key]
        else:
            diff[f'{REMOTE_VALUE}{key}'] = file1[key]
            diff[f'{ADDED_VALUE}{key}'] = file2[key]
    diff = get_string(diff)
    return diff
