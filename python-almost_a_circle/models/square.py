#!/usr/bin/python3
"""Module that contains the class Square
   that inherits from Rectangle
"""
Rectangle = __import__('models').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            elif len(args) >= 2:
                self.size = args[1]
            elif len(args) >= 3:
                self.x = args[2]
            else:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
