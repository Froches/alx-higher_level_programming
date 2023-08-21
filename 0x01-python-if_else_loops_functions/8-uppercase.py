#!/usr/bin/python3
def uppercase(str):
     for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(upper_char), end='')
        else:
            print("{}".format(char), end='')
