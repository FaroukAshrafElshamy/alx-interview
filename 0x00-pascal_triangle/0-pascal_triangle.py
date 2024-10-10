#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return ([])
    P = [[1]]
    for i in range(n - 1):
        row_size = len(P) + 1
        row = []
        for j in range(0, row_size):
            if j == 0 or j == row_size - 1:
                row.append(1)
            else:
                row.append(P[i][j] + P[i][j - 1])
        P.append(row)
    return (P)
