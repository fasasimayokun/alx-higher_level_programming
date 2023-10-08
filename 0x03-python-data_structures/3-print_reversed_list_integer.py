#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """a func that prints all ints in a list in reverse order"""
    for num in my_list[-1::-1]:
        print("{}".format(num))
