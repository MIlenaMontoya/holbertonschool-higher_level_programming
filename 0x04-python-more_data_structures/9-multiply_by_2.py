#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndic = dict()
    for a in a_dictionary:
        ndic[a] = a_dictionary[a] * 2
    return ndic