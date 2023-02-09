#!/usr/bin/python3
"""Module that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """A function that returns the dictionary description with
    simple data structure for JSON serialization of an object

    Args:
        obj : An instance of a class
    """
    return obj.__dict__
