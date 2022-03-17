import json
from os.path import abspath


def json_reader(file_path):
    """
    Reads a json file and returns a dictionary.
    """
    with open(abspath(file_path), 'r') as f:
        return json.load(f)
