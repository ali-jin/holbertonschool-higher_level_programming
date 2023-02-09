#!/usr/bin/python3
"""Module that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”

    Args:
        filename (str): The name of the json file
    """
    with open(filename) as f:
        lines = f.read()

    return json.loads(lines)
