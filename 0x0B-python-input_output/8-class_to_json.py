#!/usr/bin/python3
"""a class to json func module"""


def class_to_json(obj):
    """
    a func that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
    """
    return obj.__dict__
