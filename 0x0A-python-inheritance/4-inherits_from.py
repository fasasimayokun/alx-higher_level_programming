#!/usr/bin/python3
"""a inherits_from func module"""


def inherits_from(obj, a_class):
    '''a func that detrmins if an object is a true subclass of a class'''
    return isinstance(obj, a_class) and type(obj) != a_class
