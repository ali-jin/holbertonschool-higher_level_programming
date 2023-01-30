#!/usr/bin/python3
"""A Class Square"""


class Square:
    """Defines a square"""
    def __init__(self, __size=0):
        """Initialize the size of the square

        Args:
            __size (int): Size of the square.
        """
        self.__size = __size
        if type(__size) != int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
