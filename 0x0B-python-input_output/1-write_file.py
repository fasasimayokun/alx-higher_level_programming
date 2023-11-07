#!/usr/bin/python3
"""a write file func module"""


def write_file(filename="", text=""):
    """a func that writes a str to a text file and output the num of chars"""
    with open(filename, 'w', encoding='utf-8') as fle:
        return fle.write(text)
