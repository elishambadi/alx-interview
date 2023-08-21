#!/usr/bin/python3
"""
Rotate a 2D matrix
"""


def rotate_2d_matrix(matrix):

    """Function to rotate"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
