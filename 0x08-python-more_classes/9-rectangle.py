#!/usr/bin/python3
'''Definir class vacia con nombre rectangule'''


class Rectangle():
    '''class rectangule vacio'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangle areas
        Args:
            rect_1 (Rectangle): the first rectangular object
            rect_2 (Rectangle): the second rectangular object
        Raises:
            TypeError: if either rectangle are not instances of the
            Rectangle class
        Returns:
            rect_1 if rect_1's area is equal or greater than rect_2's
            rect_2 if rect_2's area is greater than rect_1's
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.__width * rect_1.__height
        area2 = rect_2.__width * rect_2.__height
        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a Rectangle instance with same width and height
        Args:
            size (int, optional): the size of the square instance
        """
        return cls(size, size)
