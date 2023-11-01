#!/usr/bin/python3
"""a module for prints square method"""


def print_square(size):
    """a func that prints a square # char

    Args:
        size: the size of the square
    Raises:
        TypeError: if size not int and float and is < 0
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print((('#' * size + '\n') * size), end='')


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
