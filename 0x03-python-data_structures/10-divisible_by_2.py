#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lt = []
    for a in my_list:
        if a % 2 == 0:
            new_lt.append(True)
        else:
            new_lt.append(False)
    return new_lt
