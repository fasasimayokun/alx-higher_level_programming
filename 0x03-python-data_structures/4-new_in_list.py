#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """a func that replaces an elem in a list at a
    specific position without modifying the original list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        my_new_list = my_list[:]
        my_new_list[idx] = element
        return (my_new_list)
