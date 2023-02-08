#!/usr/bin/python3
"""Module that writes in a text file"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
       and returns the number of characters written

    Args:
        filename (str): The name of the file to write in.
        text (str): The text to put in the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        NbCharacters = len(text)
        f.close

    return NbCharacters
