#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """a func that prints a matirx of ints"""
    for rw in matrix:
        for col in rw:
            if col != rw[len(rw) - 1]:
                print("{:d}".format(col), end=' ')
            else:
                print("{:d}".format(col), end='')
        print()
