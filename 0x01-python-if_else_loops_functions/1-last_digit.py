#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = number % 10
if number < 0:
    last_num = -last_num
if last_num > 5:
    print(F"Last digit of {number} is {last_num} and is greater than 5")
if last_num == 0:
    print(F"Last digit of {number} is {last_num} and is 0")
if last_num < 6 and last_num != 0:
    print(F"Last digit of {number} is {last_num} and is less than 6 and not 0")
