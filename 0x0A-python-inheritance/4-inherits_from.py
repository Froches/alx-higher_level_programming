#!/usr/bin/python3
"""To check if the object is an instance of a subclass"""


def inherits_from(obj, a_class):
    """Function that checks for inheritance"""
    obj_class = obj.__class__

    visited = set()

    while obj_class not in visited:
        if obj_class == a_class:
            return True

        visited.add(obj_class)

        obj_class = obj_class.__base__

    return False
