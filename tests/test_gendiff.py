from gendiff.gendiff import generate_diff


def test_generate_diff():
    result_json = open('tests/fixtures/json_result.txt').read()
    result_yml = open('tests/fixtures/yml_result.txt').read()
    result_stylish_json = open('tests/fixtures/nested_result.txt').read()
    result_stylish_yml = open('tests/fixtures/nested_result.txt').read()
    result_plain = open('tests/fixtures/plain_result.txt').read()
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json') == result_json
    assert generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml') == result_yml
    assert generate_diff(
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        formatter='stylish') == result_stylish_json
    assert generate_diff(
        'tests/fixtures/nested_file1.yml',
        'tests/fixtures/nested_file2.yml',
        formatter='stylish') == result_stylish_yml
    assert generate_diff(
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json',
        formatter='plain') == result_plain
