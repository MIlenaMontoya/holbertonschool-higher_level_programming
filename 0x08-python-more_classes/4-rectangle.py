#!/usr/bin/python3
'''Definir class vacia con nombre rectangule'''


class Rectangle():
    '''class rectangule vacio'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        docstring
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        docstring
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.__width + self.__height)*2

    def __str__(self):
        """Functionality for printing and using str() functions"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i is not self.__height - 1:
                rectangle.append('\n')
        return''.join(rectangle)

    def __repr__(self):
        string = []
        string.append("Rectangle(")
        string.append(str(self.__width) + ", " + str(self.__height) + ')')
        return ''.join(string)
