#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """a func that computes the square value of all
    integers of a matrix using map"""
    new_matrix = list(map(lambda nm: list(map(lambda n: n**2, nm)), matrix))
    return (new_matrix)
