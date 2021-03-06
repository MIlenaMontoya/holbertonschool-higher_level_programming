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
