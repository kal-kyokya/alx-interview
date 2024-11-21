#!/usr/bin/python3
"""
'0-rotate_2d_matrix.py' contains a function that rotates a matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a n x n matrix by 90 degrees clockwise.
    """

    for i in len(matrix):
        for j in matrix[i]:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
