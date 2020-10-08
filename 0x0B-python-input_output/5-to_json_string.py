#!/usr/bin/python3
"""[summary]
    """
import json


def to_json_string(my_obj):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    return json.dumps(my_obj, sort_keys=True
