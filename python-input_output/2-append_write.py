#!/usr/bin/python3
"""Module appends a string at the end of text file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
       and returns the number of characters added

    Args:
        filename (str): The name of the file to write in.
        text (str): The text to appends in file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        NbCharacters = len(text)
        f.close

    return NbCharacters
