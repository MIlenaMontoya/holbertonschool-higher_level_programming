#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmtx = []
    for i in matrix:
        nmtx.append(list(map(lambda a: a ** 2, i)))
    return nmtx
