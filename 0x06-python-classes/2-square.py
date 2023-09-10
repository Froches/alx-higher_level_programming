#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """The square class"""

    def __init__(self, size=0):
        """
        Initializing my new square

        Args:
            size: The size of the square
        """
        self.__size = size

        nat = isinstance(size, (float, int))
        if nat is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
