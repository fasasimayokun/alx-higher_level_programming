#!/usr/bin/python3

def magic_calculation(a, b):
    """a func that does exactly the same as the following Python bytecode:"""
    res = 0
    for nm in range(1, 3):
        try:
            if nm > a:
                raise Exception("Too far")
            res = res + a ** b / nm
        except Exception:
            res = a + b
            break
    return res
