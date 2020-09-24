#!/usr/bin/python3
'''Declaracion class Square'''


class Square():
    '''class square vacia'''

    def __init__(self, size=0, position=(0, 0)):
        '''inicializa el objeto square'''

        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for a in range(self.__position[1]):
                print("")
            for b in range(self.__size):
                for c in range(self.__position[0]):
                    print(" ", end='')
                for d in range(self.__size):
                    print("#", end='')
                print("")
