#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """a func that deletes keys with a specific value in a dictionary."""
    dic_keys = list(a_dictionary.keys())
    for key in dic_keys:
        if value == a_dictionary.get(key):
            del a_dictionary[key]
    return (a_dictionary)
