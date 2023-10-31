#!/usr/bin/python3
"""a module for matrix mul function"""


def matrix_mul(m_a, m_b):
    """a func that multiplies 2 matrices
    Args:
        m_a: the first matrix argument
        m_b: the second matrix argument
    Raises:
        TypeError: if m_a and m_b are not lists
        TypeError: if m_a or m_b are not lists of lists
        TypeError: if m_a or m_b contain a non int or float
        TypeError: if m_a or m_b are not of the same length
        ValueError: if m_a or m_b are empty lists / matrices
        ValueError: if m_a or m_b can't be multiplied
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    m_a_notmatrix = False
    m_b_notmatrix = False
    m_a_notint = False
    m_b_notint = False
    for item in m_a:
        if not isinstance(item, list):
            raise TypeError("m_a must be a list of lists")
        if len(item) != len(m_a[0]):
            m_a_notmatrix = True
        for nm in item:
            if not isinstance(nm, (int, float)):
                m_a_notint = True

    for item in m_b:
        if not isinstance(item, list):
            raise TypeError("m_b must be a list of lists")
        if len(item) != len(m_b[0]):
            m_b_notmatrix = True
        for nm in item:
            if not isinstance(nm, (int, float)):
                m_b_notint = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notint:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notint:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_notmatrix:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_notmatrix:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    results = [[] for nm in range(len(m_a))]

    for rw in range(len(m_a)):
        for cl in range(len(m_b[0])):
            x = 0
            for ky in range(len(m_b)):
                x = x + m_a[rw][ky] * m_b[ky][cl]
            results[rw].append(x)

    return results


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
