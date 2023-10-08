#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """a func that prints all ints in a list in reverse order"""
    my_list = my_list[-1::-1]
    for num in my_list:
        print("{:d}".format(num))
