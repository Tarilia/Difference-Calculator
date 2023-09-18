import json
import yaml


def make_format(path):
    _, format_file = path.split('.')
    if format_file == 'json':
        return 'json'
    if format_file == 'yaml' or format_file == 'yml':
        return 'yaml'


def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def parse_data(data, data_format):
    if data_format == 'json':
        return json.loads(data)
    if data_format == 'yaml':
        return yaml.safe_load(data)
    raise TypeError('Sorry, the data type you entered is not supported.')
