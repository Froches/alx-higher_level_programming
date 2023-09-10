#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """The square class"""

    def __init__(self, size=0):
        """
        Initializing my new square

        Args:
            size (int): The size of the square
        """
        self.size = size

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

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
