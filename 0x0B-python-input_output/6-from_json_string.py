#!/usr/bin/python3
"""[summary]
    """
import json


def from_json_string(my_str):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    return json.loads(my_str)
