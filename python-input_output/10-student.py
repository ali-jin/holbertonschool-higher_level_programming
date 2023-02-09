#!/usr/bin/python3
"""Module that contains class Student"""


class Student:
    """A class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            student_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    student_dict[key] = value
            return student_dict
        return self.__dict__
