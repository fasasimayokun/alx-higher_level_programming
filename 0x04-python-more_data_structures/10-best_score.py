#!/usr/bin/python3

def best_score(a_dictionary):
    """a func that returns a key with the biggest integer value."""
    if not a_dictionary:
        return (None)
    m = max(a_dictionary.values())
    for k, val in a_dictionary.items():
        if val == m:
            return (k)
