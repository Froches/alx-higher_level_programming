#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """The square class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing my new square

        Args:
            size (int): The size of the square
            position (int, int): Position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets and sets the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        nat = isinstance(value, int)
        if nat is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
