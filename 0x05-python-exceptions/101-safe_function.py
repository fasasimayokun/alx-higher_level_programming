#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """a func that executes a function safely"""
    try:
        return fct(*args)
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return None
