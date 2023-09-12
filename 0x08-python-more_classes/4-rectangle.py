#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle

        Args:
            width (int): The width of a rectangle
            height (int): The height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rec_str = ""
            for _ in range(self.__height):
                rec_str += '#' * self.__width + "\n"
            return rec_str.rstrip()


    def __repr__(self):
        val = f"Rectangle({self.__width}, {self.__height})"
        return val
