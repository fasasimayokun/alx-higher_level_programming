#!/usr/bin/python3
"""a to json string func module"""

import json


def to_json_string(my_obj):
    """a func that returns the json representation of an object"""
    return json.dumps(my_obj)
