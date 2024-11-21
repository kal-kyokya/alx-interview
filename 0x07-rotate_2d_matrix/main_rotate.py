#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
transpose_2d_matrix = __import__('transpose_2d_matrix').transpose_2d_matrix
rotate_2d_matrix = __import__('rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    [print(matrix[i]) for i in range(len(matrix))]
    trans_matrix = transpose_2d_matrix(matrix)
    matrx = rotate_2d_matrix(trans_matrix)
    print("\nResults:")
    [print(matrx[i]) for i in range(len(matrx))]
    print("---")

    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    [print(matrix[i]) for i in range(len(matrix))]
    trans_matrix = transpose_2d_matrix(matrix)
    matrx = rotate_2d_matrix(trans_matrix)
    print("\nResults:")
    [print(matrx[i]) for i in range(len(matrx))]
    print("---")
