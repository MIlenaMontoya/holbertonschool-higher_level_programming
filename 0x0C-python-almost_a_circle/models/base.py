#!/usr/bin/python3
"""[summary]

    Returns:
        [type]: [description]
    """
import json


class Base:
    """[summary]

    Returns:
        [type]: [description]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        if list_objs:
            n_list = [items.to_dictionary() for items in list_objs]
        else:
            n_list = []
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as work_file:
            work_file.write(Base.to_json_string(n_list))

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """[summary]

        Returns:
            [type]: [description]
        """
        if cls.__name__ is "Rectangle":
            temp = cls(3, 1)
        else:
            temp = cls(6)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """[summary]

        Returns:
            [type]: [description]
        """
        try:
            with open(cls.__name__ + ".json", "r") as work_file:
                return [
                    cls.create(**dic_new)
                    for dic_new in cls.from_json_string(work_file.read())
                ]
        except:
            return []
