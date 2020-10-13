#!/usr/bin/python3
"""[summary]
    """
# task 1 crear clase


class Base:
    """class base inicializa un objeto
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
