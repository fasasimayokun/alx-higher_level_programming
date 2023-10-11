#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """a func that computes the square value of all integers of a matrix."""
    new_matrix = [list(map(lambda x: x * x, num)) for num in matrix]
    return new_matrix
