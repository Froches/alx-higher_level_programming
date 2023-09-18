#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    A class that restricts the creation of new instance attributes,
    allowing only 'first_name' to be set.

    Attributes:
        None

    Methods:
        __setattr__(self, name, value): Sets instance
        attributes if 'name' is 'first_name'.
        Raises an AttributeError for any other attribute.
    """
    def __setattr__(self, name, value):
        """
        Set an instance attribute if 'name'
        is 'first_name', otherwise raise an error

        Args:
            name (str): The name of the attribute being set.
            value (any): The value to assign to the attribute

        Raises:
            AttributeError: If 'name' is not 'first_name'.

        Returns:
            None
        """
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            if name == '__dict__':
                err_msg = "'LockedClass' object has to attribute '__dict__'"
                raise AttributeError(err_msg)
            else:
                error_msg = f"'LockedClass' object has no attribute '{name}'"
                raise AttributeError(error_msg)
