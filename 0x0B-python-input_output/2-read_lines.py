#!/usr/bin/python3
""" Docstring """


def read_lines(filename="", nb_lines=0):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
    """

    with open(filename) as file:
        line = 0
        for i in file:
            line += 1
        if nb_lines <= 0 or nb_lines >= line:
            file.seek(0)
            for i in file:
                print(i, end="")
        else:
            file.seek(0)
            for i in range(nb_lines):
                n = file.readline()
                print(n, end="")
