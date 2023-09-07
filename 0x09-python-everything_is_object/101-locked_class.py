#!/usr/bin/python3
class LockedClass:
    """
    A class that restricts the creation of new instance attributes,
    allowing only 'first_name' to be set.

    Attributes:
        None

    Methods:
        __setattr__(self, name, value): Sets instance attributes if 'name' is 'first_name'.
                                    Raises an AttributeError for any other attribute.
    """
    def __setattr__(self, name, value):
        """
        Set an instance attribute if 'name' is 'first_name', otherwise raise an error

        Args:
            name (str): The name of the attribute being set.
            value (any): The value to assign to the attribute

        Raises:
            AttributeError: If 'name' is not 'first_name'.

        Returns:
            None
        """
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
