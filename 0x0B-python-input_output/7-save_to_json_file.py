#!/usr/bin/python3
"""[summary]
    """
import json


def save_to_json_file(my_obj, filename):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
