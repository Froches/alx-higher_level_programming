#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):
    """The class MyList that inherits from list"""

    def print_sorted(self):
        """Prints a sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
