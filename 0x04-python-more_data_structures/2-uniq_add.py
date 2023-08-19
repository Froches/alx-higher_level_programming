#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_ints = set()
    total = 0

    for num in my_list:
        if num not in unique_ints:
            total += num
            unique_ints.add(num)

    return total
