#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elemList = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            elemList += 1
        except IndexError:
            break
    print()
    return elemList
