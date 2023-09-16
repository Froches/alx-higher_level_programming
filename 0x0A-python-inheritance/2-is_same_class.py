#!/usr/bin/python3
"""Checks if an object is exactly an instance of a specified class"""


def is_same_class(obj, a_class):
    """Function that checks if object is exactly an instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
