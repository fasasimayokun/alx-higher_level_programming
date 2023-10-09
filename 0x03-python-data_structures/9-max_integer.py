#!/usr/bin/python3

def max_integer(my_list=[]):
    """a func that finds the biggest int of a list"""
    if len(my_list) == 0:
        return (None)
    else:
        m = my_list[0]
        for num in my_list:
            if num > m:
                m = num
        return (m)
