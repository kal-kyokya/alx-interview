#!/usr/bin/python3
"""
'0-transpose_2d_matrix.py' contains a function that transposes a matrix
"""

def transpose_2d_matrix(matrx):
    """
    Transposes a n x n matrix by 90 degrees clockwise.
    """
    matrix = [[0] * len(matrx[i]) for i in range(len(matrx))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = matrx[i][j]
            matrix[i][j] = matrx[j][i]
            matrix[j][i] = temp

    return matrix
