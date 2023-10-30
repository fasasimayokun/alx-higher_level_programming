#!/usr/bin/python3
"""a rectangle class template"""


class Rectangle:
    """a class Rectangle that defines a rectangle based on 0-rectangle.py"""
    def __init__(self, width=0, height=0):
        """a rectangle constructor"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """the getter method for width"""
        return self.__width

    @property
    def height(self):
        """the getter method for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """the setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """the setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area method of the rectangle class"""
        return self.__width * self.__height

    def perimeter(self):
        """the perimeter method of the rectangle class"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """the printable string representation of the object"""
        st = ""
        if self.__width != 0 and self.__height != 0:
            st += '\n'.join('#' * self.__width for nm in range(self.height))

        return st

    def __repr__(self):
        """the string representation of the object for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
