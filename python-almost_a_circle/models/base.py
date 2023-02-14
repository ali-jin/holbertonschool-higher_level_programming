#!/usr/bin/python3
"""Module that contains class Base"""
import json


class Base:
    """Class that manage id attribute in all your future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
           of list_dictionaries
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)
