#!/usr/bin/python3
"""Base Geometry class"""


class BaseGeometry:
    """A base geometry class"""
    def area(self):
        """An area class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
