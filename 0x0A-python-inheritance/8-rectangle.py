#!/usr/bin/python3
"""[summary]
    """
base_geo = __import__("7-base_geometry").BaseGeometry


class Rectangle(base_geo):
    """[summary]

    Args:
        base_geo ([type]): [description]
    """

    def __init__(self, width, height):
        """Constructor or initializer
        Arguments:
            width {[int]} -- width of the rectangle
            height {[int]} -- height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
