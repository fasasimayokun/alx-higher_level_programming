#!/usr/bin/python3
"""the square class template module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a square class inheriting from a subclass rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """the constructor for the square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''the getter method for the size attribute'''
        return self.width

    @size.setter
    def size(self, value):
        '''the setter method for the size attribute'''
        self.width = value
        self.height = value

    def __str__(self):
        """the string representation for the square class"""
        return (f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")

    def __update(self, id=None, size=None, x=None, y=None):
        """the private update method for the rectangle class"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """the update method for the object attributes"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """the dictionary form for all the square objects"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
