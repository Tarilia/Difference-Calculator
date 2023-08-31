def compare_files(file1, file2):
    diff = {}
    combined_keys = sorted(file1.keys() | file2.keys())
    for key in combined_keys:
        if key not in file1 and key in file2:
            diff[key] = {'type': 'added', 'value': file2[key]}
        elif key in file1 and key not in file2:
            diff[key] = {'type': 'deleted', 'value': file1[key]}
        elif file1[key] == file2[key]:
            diff[key] = {'type': 'unchanged', 'value': file2[key]}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = {
                'type': 'nested',
                'value': compare_files(file1[key], file2[key])
            }
        else:
            diff[key] = {'type': 'changed', 'value': {
                'old value': file1[key],
                'new value': file2[key]}}
    return diff
