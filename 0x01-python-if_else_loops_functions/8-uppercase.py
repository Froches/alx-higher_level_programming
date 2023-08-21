#!/usr/bin/python3
def uppercase(str):
    result = ""

    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(upper_char)
        else:
            result += "{}".format(char)

    print(result)
