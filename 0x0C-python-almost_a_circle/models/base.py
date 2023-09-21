#!/usr/bin/python3
"""Class Base"""


import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Implementing the json method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
