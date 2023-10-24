#!/usr/bin/python3
"""defines a magic class matching a bytecode"""

import math


class MagicClass:
    """the circle class template"""
    def __inti__(self, radius=0):
        """initializes the circle class instance
        Arg:
            radius (int or float): the radius of a new magic class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """the area method of the circle class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """the circumference method of the circle class"""
        return (2 * math.pi * self.__radius)
