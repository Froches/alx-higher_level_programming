#!/usr/bin/python3
"""A function that returns the list of attributes and methods of an object"""
def lookup(obj):
    attr_meth = dir({obj})
    avail = [item for item in attr_meth] #  if not item.startswith('_')]
    return avail
