#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 > idx >= len(my_list):
        return my_list

    new_list = []
    for num in range(len(my_list)):
        if num != idx:
            new_list.append(my_list[num])

    my_list.clear()
    my_list.extend(new_list)
    return new_list
