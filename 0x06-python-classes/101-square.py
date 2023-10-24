#!/usr/bin/python3


class Square:
    """a square class template"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes the size and position tuple
        attr of the square instanc.
        Args:
            size (int): the size of the new square class instance
            position (int, int): the position of the new square of the squ inst
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """the getter size property of the square"""
        return self.__size

    @property
    def position(self):
        """the getter of the current position of the square"""
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(nm, int) for nm in value) or
                not all(nm >= 0 for nm in value)):
            raise TypeError("position must be a tuple of 2 position integers")
        self.__position = value

    def area(self):
        """returns the area of the square instance"""
        return self.__size ** 2

    def my_print(self):
        """prints the instance of the class square"""
        if self.__size == 0:
            print("")
            return

        [print("") for nm in range(0, self.__position[1])]
        for nm in range(0, self.__size):
            [print(" ", end="") for rw in range(0, self.__position[0])]
            [print("#", end="") for cl in range(0, self.__size)]
            print("")

    def __str__(self):
        """defines the string representation of the square instance"""
        if self.__size != 0:
            [print("") for nm in range(0, self.__position[1])]
        for nm in range(0, self.__size):
            [print(' ', end='') for x in range(0, self.__position[0])]
            [print('#', end='') for y in range(0, self.__size)]
            if nm != self.__size - 1:
                print("")
        return ("")
