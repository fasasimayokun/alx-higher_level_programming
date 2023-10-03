#!/usr/bin/python3

for num in range(100):
    if num >= 0 and num <= 9:
        print("0{}, ".format(num), end='')
    elif num > 9 and num <= 98:
        print("{}, ".format(num), end='')
    elif num == 99:
        print(num)
