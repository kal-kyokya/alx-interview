#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
transpose_2d_matrix = __import__('1-transpose_2d_matrix').transpose_2d_matrix
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    transpose_2d_matrix(matrix)
    rotate_2d_matrix(matrix)
    print(matrix)
