#!/usr/bin/python3
"""a module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """a func that divides elems of matrix by div
    Args:
        matrix: list of lists conataining int or float elements
        div: the number to divide all elements of a matrix by
    Returns:
        list: the divideed matrix
    Raises:
        TypeError: if the matrix is not an int or a float
        TypeError: if the row in the matrix are not of equal size
        TypeError: if div is not a float or an int
        ZeroDivisionError: if div is 0
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for nm in row:
            if not isinstance(nm, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(nm / div, 2) for nm in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
