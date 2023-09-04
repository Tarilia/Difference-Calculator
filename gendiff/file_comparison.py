def sort_keys(first_file, second_file):
    combined_keys = sorted(first_file.keys() | second_file.keys())
    return combined_keys


def compare_files(first_file, second_file):
    diff = {}
    combined_keys = sort_keys(first_file, second_file)
    for key in combined_keys:
        if key not in first_file and key in second_file:
            diff[key] = {'type': 'added', 'value': second_file[key]}
        elif key in first_file and key not in second_file:
            diff[key] = {'type': 'deleted', 'value': first_file[key]}
        elif first_file[key] == second_file[key]:
            diff[key] = {'type': 'unchanged', 'value': second_file[key]}
        elif isinstance(first_file[key], dict) \
                and isinstance(second_file[key], dict):
            diff[key] = {
                'type': 'nested',
                'value': compare_files(first_file[key], second_file[key])
            }
        else:
            diff[key] = {'type': 'changed', 'value': {
                'old value': first_file[key],
                'new value': second_file[key]}}
    return diff
