#!/usr/bin/python3
"""function that say hi to a specific name
    """


def say_my_name(first_name, last_name=""):
    """Docstring
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        if first_name is "Doom" and last_name is "Slayer":
            print("Welcome great Slayer")
        else:
            print("My name is {:s} {:s}".format(first_name, last_name))
