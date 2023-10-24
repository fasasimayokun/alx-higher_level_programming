#!/usr/bin/python3


class Square:
    """a square template"""
    def __init__(self, size=0):
        """a constructor that checks if size is an int or a negative num"""
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
