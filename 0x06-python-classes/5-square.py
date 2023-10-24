#!/usr/bin/python3
"""the square class template"""


class Square:
    """a square class template"""
    def __init__(self, size=0):
        """initializes the size attr of the square instance

        Args:
            size: the size of the square instance
        """
        self.size = size

    @property
    def size(self):
        """the size property of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square instance"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        for rw in range(self.size):
            for col in range(self.size):
                print("#", end="\n" if col is self.size - 1 and
                      rw != col else "")
        print()
