#!/usr/bin/python3
"""print_square function that print a square"""


def print_square(size):
    """a function that a square with the size given"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
