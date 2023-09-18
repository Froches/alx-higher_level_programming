#!/usr/bin/python3
"""Class Base"""


class Base:
    """
    Represents a class Base which will act as a base class for
    other subclasses
    """

    __nb_objects = 0    # Private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
