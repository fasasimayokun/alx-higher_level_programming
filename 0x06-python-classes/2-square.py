#!/usr/bin/python3
"""the square classs template"""


class Square:
    """a square template"""
    def __init__(self, size=0):
        """a constructor that checks if size is an int or a negative num

        Args:
            size: the size of the square instance

        Raises:
            TypeError: if the size is not integer
            ValueError: if the size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
