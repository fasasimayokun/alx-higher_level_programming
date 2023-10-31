#!/usr/bin/python3
"""a module to add two integers"""


def add_integer(a, b=98):
    """adds 2 integers

    Args:
        a: the first int argument
        b: the second int argument

    Raises:
        TypeError: if a and b are not int or float

    Returns:
        the sum of the 2 ints
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.py.txt")
