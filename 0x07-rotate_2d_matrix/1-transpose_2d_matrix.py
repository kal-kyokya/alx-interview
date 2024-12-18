#!/usr/bin/python3
"""
'1-transpose_2d_matrix.py' contains a function that transposes a matrix
"""


def transpose_2d_matrix(matrx):
    """
    Transposes a n x n matrix by 90 degrees clockwise.
    """
    matrix = matrx

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
