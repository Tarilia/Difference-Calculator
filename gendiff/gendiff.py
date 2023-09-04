from gendiff.parsing import parse_files
from gendiff.file_comparison import compare_files
from gendiff.formatters.stylish import get_format_stylish


def get_format(diff, formatter):
    if formatter == 'stylish':
        diff = f"{{\n{get_format_stylish(diff)}}}"
    return diff


def generate_diff(path1, path2, formatter='stylish'):
    file1 = parse_files(path1)
    file2 = parse_files(path2)
    diff = compare_files(file1, file2)
    diff = get_format(diff, formatter)
    return diff
