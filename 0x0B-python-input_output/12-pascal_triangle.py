#!/usr/bin/python3
"""a pascal_triangle func"""


def pascal_triangle(n):
    """a func that represent pascal's triangle of size n
    and returns a matrix of ints representing a triangle
    """
    if n <= 0:
        return []

    tri_angles = [[1]]
    while len(tri_angles) != n:
        trian = tri_angles[-1]
        aux = [1]
        for nm in range(len(trian) - 1):
            aux.append(trian[nm] + trian[nm + 1])
        aux.append(1)
        tri_angles.append(aux)
    return tri_angles
