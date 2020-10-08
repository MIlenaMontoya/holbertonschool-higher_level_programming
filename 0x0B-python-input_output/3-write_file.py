#!/usr/bin/python3
""" Docstring """


def write_file(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
    """
    with open(filename, 'w') as file:
        return file.write(text)
