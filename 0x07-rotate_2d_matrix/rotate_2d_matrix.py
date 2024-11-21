#!/usr/bin/python3
"""
'0-rotate_2d_matrix.py' contains a function that rotates a matrix
"""


def rotate_2d_matrix(matrx):
    """
    Rotates a n x n matrix by 90 degrees clockwise.
    """
    matrix = [[0] * len(matrx[i]) for i in range(len(matrx))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = matrx[i][j]
            matrix[i][j] = matrx[i][-1 - j]
            matrix[i][-1 - j] = temp

    return matrix
