#!/usr/bin/python3

class Square:
    """a square class template"""
    def __init__(self, size=0):
        """initializes the size attr of the square class instance"""
        self.size = size

    @property
    def size(self):
        """the size property/attribute of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a method that returns the area of the square"""
        return self.__size ** 2
