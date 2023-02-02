#!/usr/bin/python3
"""Module that contains class Rectangle"""


class Rectangle:
    """A class that define a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the width and height of the rectangle

        Args:
            width (int, optional): Width of the rectangle.
            height (int, optional): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property of the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the value of the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property of the height of the rectangle """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
