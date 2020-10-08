#!/usr/bin/python3
"""[summary]
    """
import json


def load_from_json_file(filename):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    with open(filename, 'r') as file:
        objet_json = json.load(file)
        return objet_json
