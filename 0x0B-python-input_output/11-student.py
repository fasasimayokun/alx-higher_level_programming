#!/usr/bin/python3
"""a student class template"""


class Student:
    """the student class"""
    def __init__(self, first_name, last_name, age):
        """initializes the class student instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        a func that retrieves a dictionary
        representation of a Student instance
        """
        try:
            for atr in attrs:
                if not isinstance(atr, str):
                    return self.__dict__
        except Exception:
            return self.__dict__
        _dict = dict()
        for ky, val in self.__dict__.items():
            if ky in attrs:
                _dict[ky] = val
        return _dict

    def reload_from_json(self, json):
        """a func that replaces all attrs of the student objects with the
        ones in the json args
        """
        for ky, val in json.items():
            if ky in self.__dict__:
                self.__dict__[ky] = val
