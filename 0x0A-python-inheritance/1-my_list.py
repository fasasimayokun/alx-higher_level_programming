#!/usr/bin/python3
"""a mylist class template"""


class MyList(list):
    """a custom mylist template"""
    def print_sorted(self):
        '''a func that prints a sorted list'''
        print(sorted(self))
