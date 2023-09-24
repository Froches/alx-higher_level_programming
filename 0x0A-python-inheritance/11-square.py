#!/usr/bin/python3
"""Defines a Square class that inherits from the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square class"""

    def __init__(self, size):
        """Initializes a square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String initialization"""
        return f"[Square] {self.__size}/{self.__size}"
