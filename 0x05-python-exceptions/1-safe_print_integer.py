#!/usr/bin/python3
def safe_print_integer(value):

    try:
        print("{:d}".format(value), end='')
        print()
        if value != 0:
            return True
    except ValueError:
        return False
