#!/usr/bin/python3
"""Module that read and print a text file"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
       and prints it to stdout

    Args:
        filename (str): A text file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
