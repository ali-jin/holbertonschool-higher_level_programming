#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newMatrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j**2)
        newMatrix.append(row)
    return newMatrix
