#!/usr/bin/python3
"""a lookup func module"""


def lookup(obj):
    """a func that looks up an object attrs and methods presents in a class
    Args:
        obj (object): the object of the list
    Returns:
        list: all the list of attrs
    """
    return dir(obj)
