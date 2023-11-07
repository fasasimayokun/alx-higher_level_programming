#!/usr/bin/python3
"""a from json string func module"""

import json


def from_json_string(my_str):
    """returns a object represented by json string"""
    return json.loads(my_str)
