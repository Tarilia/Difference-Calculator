from gendiff.gendiff import generate_diff


def test_generate_diff_json():
    path = 'tests/fixtures/json_result.txt'
    with open(path, 'r') as file:
        result = file.read()
        assert generate_diff(
                'tests/fixtures/file1.json', 
                'tests/fixtures/file2.json'
                ) == result


def test_generate_diff_yml():
    path = 'tests/fixtures/yml_result.txt'
    with open(path, 'r') as file:
        result = file.read()
        assert generate_diff(
                'tests/fixtures/file1.yml',
                'tests/fixtures/file2.yml'
                ) == result


def test_generate_diff_nested_json():
    path = 'tests/fixtures/nested_result.txt'
    with open(path, 'r') as file:
        result = file.read()
        assert generate_diff(
                'tests/fixtures/nested_file1.json',
                'tests/fixtures/nested_file2.json'
                ) == result


def test_generate_diff_nested_yml():
    path = 'tests/fixtures/nested_result.txt'
    with open(path, 'r') as file:
        result = file.read()
        assert generate_diff(
                'tests/fixtures/nested_file1.yml',
                'tests/fixtures/nested_file2.yml',
		formatter='stylish'
                ) == result
