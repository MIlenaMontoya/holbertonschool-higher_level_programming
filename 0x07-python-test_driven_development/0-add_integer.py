#!/usr/bin/python3
"""
Write a function that adds 2 integers


"""


def add_integer(a, b=98):
    """function that adds 2 integers or floats
    whit paramethers type int.
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
