import json
import yaml


def make_format(path):
    _, format_file = path.split('.')
    return format_file


def open_json_file(path):
    return json.load(open(path))


def open_yaml_file(path):
    return yaml.safe_load(open(path))


def parse_files(path):
    format_file = make_format(path)
    if format_file == 'json':
        return open_json_file(path)
    if format_file == 'yaml' or format_file == 'yml':
        return open_yaml_file(path)
