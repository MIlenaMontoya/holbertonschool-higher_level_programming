#!/usr/bin/python3
""" Docstring """


def number_of_lines(filename=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
    """

    line = 0
    with open(filename, encoding="utf-8") as file:
        for i in file:
            line += 1
    return line
