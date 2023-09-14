from gendiff.parsing import make_format, parse_files, read_file
from gendiff.file_comparison import compare_files
from gendiff.formatters.stylish import get_format_stylish
from gendiff.formatters.plain import get_format_plain
from gendiff.formatters.json import get_format_json


def get_format(diff, formatter):
    if formatter == 'stylish':
        diff = get_format_stylish(diff)
    if formatter == 'plain':
        diff = get_format_plain(diff)
    if formatter == 'json':
        diff = get_format_json(diff)
    return diff


def generate_diff(first_path, second_path, formatter='stylish'):
    first_format = make_format(first_path)
    second_format = make_format(second_path)
    first_file = parse_files(read_file(first_path), first_format)
    second_file = parse_files(read_file(second_path), second_format)
    diff = compare_files(first_file, second_file)
    diff = get_format(diff, formatter)
    return diff
