#!/usr/bin/python3
"""a script for find peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """a func that finds a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
