#!/usr/bin/python3
"""[summary]
    """
# task 2 crear clase rectangulo que herede clase Base
from models.base import Base


class Rectangle(Base):
    """class Rectangle

    Args:
        hereda la clase Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__width

# task 3 validar atributos
    @width.setter
    def width(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

# task 4
    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__width * self.__height

# task 5 y task 7
    def display(self):
        for a in range(self.__y):
            print()
        for b in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

'''# task 6
# falta hacer toda la tarea
    def __str__(self):
        self.__str__

# task 8
# task 9 agregar kwargs a los argumentos de la funcion
    def update(self, *args, **kwargs):
        self.width == 2
        self.height == 3
        self.x == 4
        self.y == 5

# task 13
    def to_dictionary(self):
        self.id
        self.width
        self.height
        self.x
        self.y
'''