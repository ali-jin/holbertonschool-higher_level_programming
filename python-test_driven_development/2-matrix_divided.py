#!/usr/bin/python3
"""function matrix_divided that divides a matrix"""


def matrix_divided(matrix, div):
    """the function divides all elements in the matrix"""

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [num for row in matrix for num in row])):
        mes = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(mes)

    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    else:
        res = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
        return res
