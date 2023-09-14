import pytest
from gendiff.gendiff import generate_diff
from gendiff.parsing import read_file


file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yml = 'tests/fixtures/file1.yml'
file2_yml = 'tests/fixtures/file2.yml'
nested_file1_json = 'tests/fixtures/nested_file1.json'
nested_file2_json = 'tests/fixtures/nested_file2.json'
nested_file1_yml = 'tests/fixtures/nested_file1.yml'
nested_file2_yml = 'tests/fixtures/nested_file2.yml'

result_json = 'tests/fixtures/json_result.txt'
result_yml = 'tests/fixtures/yml_result.txt'
result_stylish_json = 'tests/fixtures/nested_result.txt'
result_stylish_yml = 'tests/fixtures/nested_result.txt'
result_plain = 'tests/fixtures/plain_result.txt'
nested_result_json = 'tests/fixtures/nested_json_result.txt'


@pytest.mark.parametrize('first_file, second_file, formatter, result_file',
                         [(file1_json, file2_json, 'stylish',
                           read_file(result_json)),
                          (file1_yml, file2_yml, 'stylish',
                           read_file(result_yml)),
                          (nested_file1_json, nested_file2_json, 'stylish',
                           read_file(result_stylish_json)),
                          (nested_file1_yml, nested_file2_yml, 'stylish',
                           read_file(result_stylish_yml)),
                          (nested_file1_json, nested_file2_json, 'plain',
                           read_file(result_plain)),
                          (nested_file1_yml, nested_file2_yml, 'plain',
                           read_file(result_plain)),
                          (nested_file1_json, nested_file2_json, 'json',
                           read_file(nested_result_json)),
                          (nested_file1_yml, nested_file2_yml, 'json',
                           read_file(nested_result_json))])
def test_generate_diff(first_file, second_file, formatter, result_file):
    assert generate_diff(first_file, second_file, formatter) == result_file
