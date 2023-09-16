#!/usr/bin/python3
"""Adds two ints"""

def add_integer(a, b=98):
    """
    Returns a+b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
