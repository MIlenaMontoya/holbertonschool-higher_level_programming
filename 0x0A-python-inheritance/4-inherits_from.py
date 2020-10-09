#!/usr/bin/python3
"""[summary]
    """


def inherits_from(obj, a_class):
    """[summary]

    Args:
        obj ([type]): [description]
        a_class ([type]): [description]
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
