from gendiff.gendiff import generate_diff


def test_generate_diff():
    file1_json = 'tests/fixtures/file1.json'
    file2_json = 'tests/fixtures/file2.json'
    file1_yml = 'tests/fixtures/file1.yml'
    file2_yml = 'tests/fixtures/file2.yml'
    nested_file1_json = 'tests/fixtures/nested_file1.json'
    nested_file2_json = 'tests/fixtures/nested_file2.json'
    nested_file1_yml = 'tests/fixtures/nested_file1.yml'
    nested_file2_yml = 'tests/fixtures/nested_file2.yml'

    result_json = open('tests/fixtures/json_result.txt').read()
    result_yml = open('tests/fixtures/yml_result.txt').read()
    result_stylish_json = open('tests/fixtures/nested_result.txt').read()
    result_stylish_yml = open('tests/fixtures/nested_result.txt').read()
    result_plain = open('tests/fixtures/plain_result.txt').read()
    nested_result_json = open('tests/fixtures/nested_json_result.txt').read()

    assert generate_diff(file1_json, file2_json) == result_json
    assert generate_diff(file1_yml, file2_yml) == result_yml
    assert generate_diff(nested_file1_json, nested_file2_json,
                         formatter='stylish') == result_stylish_json
    assert generate_diff(nested_file1_yml, nested_file2_yml,
                         formatter='stylish') == result_stylish_yml
    assert generate_diff(nested_file1_json, nested_file2_json,
                         formatter='plain') == result_plain
    assert generate_diff(nested_file1_yml, nested_file2_yml,
                         formatter='plain') == result_plain
    assert generate_diff(nested_file1_json, nested_file2_json,
                         formatter='json') == nested_result_json
    assert generate_diff(nested_file1_yml, nested_file2_yml,
                         formatter='json') == nested_result_json
