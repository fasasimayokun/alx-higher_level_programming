#!/usr/bin/python3
"""the square class template"""


class Square:
    """a square class with private instance attribute size"""
    def __init__(self, size):
        """constructor initializing the private size attr

        Args:
            size: the size of the square instance
        """
        self.__size = size
