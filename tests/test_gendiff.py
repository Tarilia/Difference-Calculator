from gendiff.gendiff import generate_diff


def test_generate_diff():
    path = 'tests/fixtures/json_result.txt'
    with open(path, 'r') as file:
        result = file.read()
        assert generate_diff(
                'tests/fixtures/file1.json', 
                'tests/fixtures/file2.json'
                ) == result

