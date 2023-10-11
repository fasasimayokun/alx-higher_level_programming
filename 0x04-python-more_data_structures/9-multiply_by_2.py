#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """a func that returns a new dictionary with all values multiplied by 2"""
    new_dict = {}
    for num in a_dictionary:
        new_dict[num] = a_dictionary[num] * 2
    return (new_dict)
