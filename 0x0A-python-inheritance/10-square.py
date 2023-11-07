#!/usr/bin/python3
"""a rectangle class template"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''a child class representing a rectangle'''
    def __init__(self, size):
        '''the constructor for the square child class'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """the area method for the square class"""
        return self.__size * self.__size
