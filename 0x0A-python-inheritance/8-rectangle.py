#!/usr/bin/python3
"""a rectangle class template"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''a child class representing a rectangle'''
    def __init__(self, width, height):
        '''the rectangle child class constructor'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
