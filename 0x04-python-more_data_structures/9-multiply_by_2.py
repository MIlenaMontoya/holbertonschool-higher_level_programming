#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = dict(a_dictionary)
    for a in a_dictionary:
        newDic[a] = a_dictionary[a] * 2
    return newDic
