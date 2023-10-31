#!/usr/bin/python3
"""a module that multiples 2 matrices using numpy"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """a func that multiplies 2 matrices
    Args:
        m_a: the first matrix argument
        m_b: the second matrix argument
    Returns:
        returns m_a * m_b
    """

    return numpy.matmul(m_a, m_b)
