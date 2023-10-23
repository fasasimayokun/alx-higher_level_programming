#!/usr/bin/python3

def safe_print_division(a, b):
    """a func that div two ints and prints the result."""
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
