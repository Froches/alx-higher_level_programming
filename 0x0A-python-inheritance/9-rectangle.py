#!/usr/bin/python3
"""A rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The rectangle class"""

    def __init__(self, width, height):
        """Initializing a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """The area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Defines the string representation of the Rectangle class"""
        return f"[Rectangle] {self.__width}/{self.__height}"
