#!/usr/bin/python3
"""Module that contains the class Square
   that inherits from Rectangle
"""
Rectangle = __import__('models').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def area(self):
        """area of square"""
        return self.size * self.size

    def display(self):
        """Print the rectangle"""
        for line in range(self.y):
            print("")
        for row in range(self.size):
            print((" " * self.x) + ('#' * self.size))

    def __str__(self):
        id = self.id
        size = self.size
        x = self.x
        y = self.y
        return '[Square] (%s) %s/%s - %s' % (id, x, y, size)
