#!/usr/bin/python3
"""A Class Square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size of the square

        Args:
            __size (int): Size of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: the area of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property of square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """proprety position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """proprety setter position of square"""
        if type(value[0]) != int or type(value[1] != int) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            print("")
