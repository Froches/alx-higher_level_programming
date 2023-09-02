#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):  # Iterate through the first x elements of the list
            if isinstance(my_list[i], int):  # Check if the item is an integer
                print("{:d}".format(my_list[i]), end=' ')
                count += 1
    except (ValueError, TypeError):
        pass  # Handle exceptions by doing nothing
    print()
    return count
