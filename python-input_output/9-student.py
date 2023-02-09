#!/usr/bin/python3
"""Module that contains class Student"""


class Student:
    """A class that contains information of students
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
