#!/usr/bin/python3
"""Defines a Square class that inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method for the square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
