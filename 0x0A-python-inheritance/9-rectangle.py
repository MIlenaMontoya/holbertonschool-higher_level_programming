#!/usr/bin/python3
"""[summary]

    Returns:
        [type]: [description]
    """
base_geo = __import__("7-base_geometry").BaseGeometry


class Rectangle(base_geo):
    """[summary]

    Args:
        base_geo ([type]): [description]
    """

    def __init__(self, width, height):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
