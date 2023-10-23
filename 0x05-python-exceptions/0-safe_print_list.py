#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """a func that prints x elements of a list"""
    y = 0
    try:
        for nm in range(x):
            print(my_list[nm], end='')
            y += 1
    except IndexError:
        None
    print()
    return y
