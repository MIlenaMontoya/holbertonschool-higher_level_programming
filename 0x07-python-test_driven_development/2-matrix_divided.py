#!/usr/bin/python3
'''Write a function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''function that divide all elements
    whit arguments '''

    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    size_len = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for num_list in row:
            if type(num_list) is not int and type(num_list) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of '
                    'integers/floats')
        if size_len == 0:
            size_len = len(row)
        elif size_len != len(row):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(num_list / div, 2) for num_list in row] for row in matrix]
