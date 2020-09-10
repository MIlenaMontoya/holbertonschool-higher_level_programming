#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ns = []
    for a in my_list:
        if a == search:
            ns.append(replace)
        else:
            ns.append(a)
    return ns
