#!/usr/bin/python3
"""say_my_name is a function to print your name"""


def say_my_name(first_name, last_name=""):
    """a function that print your name"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
