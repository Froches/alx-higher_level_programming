#!/usr/bin/python3
"""Defining a Rectangle class with all its methods and attributes"""


class Rectangle:
    """The Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                rec_str += str(self.print_symbol) * self.__width + "\n"
            return rec_str.rstrip()

    def __repr__(self):
        val = f"Rectangle({self.__width}, {self.__height})"
        return val

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
