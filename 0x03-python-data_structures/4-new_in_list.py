#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_lt = my_list.copy()
        new_lt[idx] = element
        return new_lt
