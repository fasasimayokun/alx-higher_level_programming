#!/usr/bin/python3
"""a load from json file func module"""

import json


def load_from_json_file(filename):
    """a func that creates an ojbect from a json file"""
    with open(filename, 'r', encoding='utf-8') as fle:
        return json.load(fle)
