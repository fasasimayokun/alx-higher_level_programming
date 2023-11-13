#!/usr/bin/python3
"""the Rectangle class template module"""

from models.base import Base


class Rectangle(Base):
    """the Rectangle class inheriting from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """the rectangle constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """the getter method for the width private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter method for the width private attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """the getter method for the height private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """the setter method for the height private attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """the getter method for the x private attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """the setter method for the x private attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the getter method for the y private attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """the setter method for the y private attribute and validator"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """the area method of the rectangle class"""
        return self.__width * self.__height

    def display(self):
        """the prints method that display the rectangle in # chars"""
        rect = ("\n" * self.__y +
                (' ' * self.__x + '#' * self.__width + '\n') * self.__height)
        print(rect, end="")

    def __str__(self):
        """the string magic method representation for the rectangle class"""
        return (f"[{type(self).__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """the private update method for the rectangle class"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
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
        """the dictionary form for all the rectangle objects"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
