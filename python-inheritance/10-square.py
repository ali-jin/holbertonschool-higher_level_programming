#!/usr/bin/python3
"""Module that contains the class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from class Rectangle"""
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.__size = size
        self.integer_validator("width", self.__size)

    def area(self):
        return self.__size * self.__size
