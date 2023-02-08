#!/usr/bin/python3
"""Module that transform object in JSON representation"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON
    representation of an object (string)

    Args:
        my_obj (str): The string to transform
    """
    json_string = json.dumps(my_obj)
    print(json_string)
    print(type(json_string))
