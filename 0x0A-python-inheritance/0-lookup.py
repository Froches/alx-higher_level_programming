#!/usr/bin/python3
"""A function that returns the list of attributes and methods of an object"""


def lookup(obj):
    """The lookup function.
    Args:
        obj: object passed whose attributes we're to find
    """

    attr_meth = dir({obj})
    avail = [item for item in attr_meth]
    return avail
