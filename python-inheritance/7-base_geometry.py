#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""


class BaseGeometry:
    """A class BaseGeometry"""
    def __init__(self, name="", value=0):
        self.name = name
        self.value = value

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name

        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
