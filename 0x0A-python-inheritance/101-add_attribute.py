#!/usr/bin/python3
"""a func that adds attrs to an object"""


def add_attribute(obj, atr, val):
    """a func that adds a new attr to an object
    Args:
        obj (any): the object to add
        atr (str): the name of attr to add to the object
        val (any): the value of the attr
    Raises:
        TypeError: if the attr can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, val)
