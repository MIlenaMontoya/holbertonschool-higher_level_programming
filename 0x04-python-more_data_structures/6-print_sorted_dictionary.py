#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dic in sorted(a_dictionary.keys()):
        print("{}: {}".format(dic, a_dictionary[dic]))
