#!/usr/bin/python3
"""Function that adds a new attribute to an object if possible"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to object if possible, or raises TypeError
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
