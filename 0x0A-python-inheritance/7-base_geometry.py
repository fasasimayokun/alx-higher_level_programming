#!/usr/bin/python3
'''a basegeometry class template'''


class BaseGeometry:
    '''a basegeometry template'''
    def area(self):
        """a func that returns the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """a func that validates the values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
