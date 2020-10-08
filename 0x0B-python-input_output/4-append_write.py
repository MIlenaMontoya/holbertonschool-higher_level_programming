#!/usr/bin/python3
"""[summary]
    """

def append_write(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    with open(filename, 'a') as file:
        return file.write(text)
