#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """a func that finds all multiples of 2 in a list."""
    new_list = my_list[:]
    for num in range(len(new_list)):
        if new_list[num] % 2 == 0:
            new_list[num] = True
        else:
            new_list[num] = False
    return (new_list)
