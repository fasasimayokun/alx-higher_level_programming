#!/usr/bin/python3
"""a rectangle class template"""


class Rectangle:
    """a class Rectangle that defines a rectangle based on 0-rectangle.py"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """a rectangle constructor"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """the setter method for width
        Raises:
            TypeError: if width is not an int
            ValueError: if width is < 0
        """
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
        if not self.width or not self.height:
            return ''

        return ((str(self.print_symbol) * self.width + '\n') *
                self.height)[:-1]

    def __repr__(self):
        """the string representation of the object for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every object deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the greater of the 2 rectangles
        Args:
            rect_1: the first rect
            rect_2: the second rect
        Raises:
            TypeError: if rect_1 and 2 are not instance of rectangle
        Returns:
            the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2
