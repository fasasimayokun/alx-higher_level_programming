#!/usr/bin/python3
"""a save to json file func module"""

import json


def save_to_json_file(my_obj, filename):
    """a func that writes an object to a text file using json representation"""
    with open(filename, 'w', encoding='utf-8') as fle:
        json.dump(my_obj, fle)
