#!/usr/bin/python3
"""
'0-rotate_2d_matrix.py' contains a function that rotates a matrix
"""


def rotate_2d_matrix(matrx):
    """
    Rotates a n x n matrix by 90 degrees clockwise.
    """
    matrix = matrx

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][-1 - j]
            matrix[i][-1 - j] = temp
