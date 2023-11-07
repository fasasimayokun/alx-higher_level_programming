#!/usr/bin/python3
"""a class student template"""


class Student:
    """the class student template"""
    def __init__(self, first_name, last_name, age):
        """initializes the student instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a func that returns the dictionary repr of a student object"""
        return self.__dict__
