#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """a func  that prints a dictionary by orderd keys."""
    new_dict = sorted(a_dictionary)
    for stg in new_dict:
        print("{}: {}".format(stg, a_dictionary[stg]))
