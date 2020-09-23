#!/usr/bin/python3
'''Declaracion class Square'''


class Square():
    '''class square vacia'''

    def __init__(self, size=0):
        '''constructor de objeto
        con arg. '''

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    '''metodo get define contructor que
    optiene el valor size'''

    @property
    def size(self):
        return self.__size

    '''metodo set que pone el valor y lo valida
    segun el tipo de dato'''

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    '''crear nuevo constructor que
     retorna el area de un cuadrado'''

    def area(self):
        return self.__size ** 2
