#!/usr/bin/python3
"""The function add_integer()"""


def add_integer(a, b=98):
    """"Return the function of a + b"""
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
