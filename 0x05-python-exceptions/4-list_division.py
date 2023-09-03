#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            elem1 = my_list_1[i] if i < len(my_list_1) else 0
            elem2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(elem1, (int, float)) or not isinstance(elem2, (int, float)):
                print("wrong type")
                new_list.append(0)
            elif elem2 == 0:
                print("out of range")
                new_list.append(0)
            else:
                new_list.append(elem1 / elem2)

    except IndexError:
            print("division by 0")
            new_list.append(0)
    finally:
        pass

    return new_list
