#!/usr/bin/python3
"""a myint class template"""


class MyInt(int):
    """a class that inherits from int, the rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """a method that creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """the magic method of equal operator changing to not equal"""
        return int(self) != other

    def __ne__(self, other):
        """the magic method of not equal operator changing to equal"""
        return int(self) == other
