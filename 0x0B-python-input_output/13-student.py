#!/usr/bin/python3
"""[summary]
    """


class Student:
    """[summary]
    """

    def __init__(self, first_name, last_name, age):
        """[summary]

        Args:
            first_name ([type]): [description]
            last_name ([type]): [description]
            age ([type]): [description]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            new_dic = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dic[i] = getattr(self, i)
            return new_dic
        return self.__dict__
