#!/usr/bin/python3
"""Module that write object in text file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
       using a JSON representation

    Args:
        my_obj : The object to write
        filename (str): The name of the text file
    """
    with open(filename, 'w') as f:
        json_representation = json.dumps(my_obj)
        f.write(json_representation)
        f.close
