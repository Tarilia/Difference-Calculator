from gendiff.parsing import parse_files
from gendiff.file_comparison import compare_files
from gendiff.stylish import convert_to_format_stylish


def generate_diff(path1, path2):
    file1 = parse_files(path1)
    file2 = parse_files(path2)
    diff = compare_files(file1, file2)
    diff = f"{{\n{convert_to_format_stylish(diff)}}}\n"
    return diff
