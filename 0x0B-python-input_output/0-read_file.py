#!/usr/bin/python3
"""a read_file function module"""


def read_file(filename=""):
    """a func that reads a file and prints it to the stdout"""
    with open(filename, encoding='utf-8') as fl:
        print(fl.read(), end='')
