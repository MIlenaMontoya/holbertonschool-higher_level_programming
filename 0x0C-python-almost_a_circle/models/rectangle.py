#!/usr/bin/python3
"""[summary]
    """
# task 2 crear clase rectangulo que herede clase Base
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
         return self.__width

    @width.setter  #task 3 validar atributos
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

# task 4 
    def area(self):
        return self.width * self.height

# task 5 y task 7
    def display(self):
        for a in range(self.y):
            print("")
        for b in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

# task 6
    def __str__(self):
        self.__str__ # falta hacer toda la tarea 

# task 8
    def update(self, *args, **kwargs): # task 9 agregar kwargs a los argumentos de la funcion 
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
