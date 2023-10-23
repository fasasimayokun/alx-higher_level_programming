#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """a func that  prints the first x elements of a list and only ints"""
    y = 0
    for nm in range(x):
        try:
            print("{:d}".format(my_list[nm]), end='')
            y += 1
        except (ValueError, TypeError):
            pass
    print()
    return y
