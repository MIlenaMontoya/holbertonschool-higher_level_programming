#!/usr/bin/python3
"""[summary]
    """


class BaseGeometry:
    """
    docstring
    """
    def area(self):
        """[summary]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
