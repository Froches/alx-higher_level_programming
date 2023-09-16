#!/usr/bin/python3
"""Function that checks if an object is an instance of a class or its parent class"""

def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or one that inherited from that class"""
    if isinstance(obj, a_class):
        return True
    return False
