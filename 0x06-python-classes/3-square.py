#!/usr/bin/python3


class Square:
    """the square class template"""
    def __init__(self, size=0):
        """a constructor that initializes the instance of the square class
        only if it is an int and it >= 0

        Args:
            size: the size of the square instance

        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """the area method of the square class that return the square
        of the given size

        Returns:
            the squared value of the size
        """
        return self.__size ** 2
