#!/usr/bin/python3
"""Class that inherits from an inbuilt class"""


class MyInt(int):
    """Class that inherits from int class and modifies it"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
