#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """a func that prints an int"""
    val_is_int = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        val_is_int = False
    return val_is_int
