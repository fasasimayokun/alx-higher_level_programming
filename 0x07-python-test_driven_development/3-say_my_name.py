#!/usr/bin/python3
"""module for the say my name func"""


def say_my_name(first_name, last_name=""):
    """a func that prints the first and last name
    Args:
        first_name: the first name argument of the func
        last_name: the last name argument of the func
    Raises:
        TypeError: if first and last name aren't strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
