#!/usr/bin/python3

def multiple_returns(sentence):
    """a func that returns a tuple with the len of a str and its 1st char."""
    if len(sentence) == 0:
        return (None)
    return (len(sentence), sentence[0])
