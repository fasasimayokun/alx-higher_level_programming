#!/usr/bin/python3
"""a append write func module"""


def append_write(filename="", text=""):
    """
    a fucn that appends a text to the end of a file and
    print the num of chars
    """
    with open(filename, "a", encoding='utf-8') as fle:
        return fle.write(text)
