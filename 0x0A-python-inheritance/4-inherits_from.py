#!/usr/bin/python3
"""To check if the object is an instance of a subclass"""


def inherits_from(obj, a_class):
    """Function that checks for inheritance"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
