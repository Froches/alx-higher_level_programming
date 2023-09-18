#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Class with no class or object attribute, that prevents the user
    from dynamically creating attributes except if the new attribute is
    called 'first_name'
    """
    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = None
