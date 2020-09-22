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

    '''crear nuevo constructor'''
    def area(self):
        return self.__size * self.__size

    '''aqui va otro comentario'''
    def size(self):
        return self.__size

    '''otro definicion'''
    def size(self, value):
        self.__size = size
