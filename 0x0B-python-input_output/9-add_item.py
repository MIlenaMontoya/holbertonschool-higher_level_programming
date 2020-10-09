#!/usr/bin/python3
"""[summary]
    """
import sys
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file
try:
    l = load("add_item.json")
except:
    l = []
l += sys.argv[1:]
save(l, "add_item.json")
