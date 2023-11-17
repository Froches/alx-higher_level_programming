#!/usr/bin/python3
"""Adds two ints"""

def add_integer(a, b=98):
    """
    This function adds two integers
    It works with integers

    >>> add_integer(2, 3)
    5

    >>> add_integer(-1, 1)
    0

    >>> add_integer(0, 0)
    0

    But does not work with strings or characters

    >>> add_integer('s', 10)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 3, in add_integer
    TypeError: a must be an integer

    >>> add_integer(5, 'g')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 5, in add_integer
    TypeError: b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
