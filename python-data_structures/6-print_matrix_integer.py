#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix is not None:
        for row in matrix:
            for List in row:
                print("{:d}".format(List), end='')
                if row.index(List) != len(row) - 1:
                    print(" ", end="")
                if row.index(List) == len(row) - 1:
                    print("")
    if (matrix == [[]]):
        print("")
