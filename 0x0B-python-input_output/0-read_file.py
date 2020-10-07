#!/usr/bin/python3
""" Docstring """


def read_file(filename=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
