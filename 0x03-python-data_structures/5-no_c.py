#!/usr/bin/python3
def no_c(my_string):
    new_s = ''
    for a in my_string:
        if a != 'C' and a != 'c':
            new_s = new_s + a
    return new_s
