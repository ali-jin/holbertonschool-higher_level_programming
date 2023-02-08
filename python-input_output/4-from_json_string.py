#!/usr/bin/python3
"""Module that transforms a JSON string to object"""
import json


def from_json_string(my_str):
    """A function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (str): The JSON string to transforms
    """
    return json.loads(my_str)
