#!/usr/bin/python3
"""
a script that adds all args to a Python list, and then save them to a file:
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args_list = list(sys.argv[1:])

try:
    prev_data = load_from_json_file('add_item.json')
except Exception:
    prev_data = []

prev_data.extend(args_list)
save_to_json_file(prev_data, 'add_item.json')
