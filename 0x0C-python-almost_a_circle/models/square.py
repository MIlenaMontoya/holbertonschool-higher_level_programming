#!/usr/bin/python3
"""[summary]
    """
# task 10
from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """

    def __init__(self, size, x=0, y=0, id=None):
        """[summary]

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

# task 11
    @property
    def size(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        self.width = value
        self.height = value

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        str_id = str(self.id)
        str_height = str(self.height)
        str_x = str(self.x)
        str_y = str(self.y)
        str_new = "[Square] (" + str_id + ") " + str_x + "/" + str_y + " - "
        str_new = str_new + str_height
        return str_new

# task 12
    def update(self, *args, **kwargs):
        """[summary]
        """
        if args:
            index = 0
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                    self.height = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y,
        }
