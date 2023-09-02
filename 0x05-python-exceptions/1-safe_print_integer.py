#!/usr/bin/python3

def safe_print_integer(value):
    try:
        formatted_value = ("{:d}".format(int(value)))
        print(formatted_value)
        return True
    except (ValueError, TypeError):
        return False
