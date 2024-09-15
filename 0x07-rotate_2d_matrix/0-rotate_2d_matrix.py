#!/usr/bin/python3

"""
Rotate the Matrix
Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix by 90 degrees in place."""
    Length = len(matrix)
    for row in range(Length // 2):
        Row = Length - row - 1
        for column in range(row, Row):
            Column = Length - column - 1
            Temp = matrix[row][column]
            matrix[row][column] = matrix[Column][row]
            matrix[Column][row] = matrix[Row][Column]
            matrix[Row][Column] = matrix[column][Row]
            matrix[column][Row] = Temp
