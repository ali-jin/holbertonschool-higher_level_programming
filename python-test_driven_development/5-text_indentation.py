#!/usr/bin/python3
"""text_indentation that print text"""


def text_indentation(text):
    """a function that print text witn indentation"""
    line = ""
    list_char = ['.', '?', ':']

    if type(text) != str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if line == "" and text[i] == " ":
            pass
        elif text[i] in list_char:
            line += text[i]
            print(line, end="\n\n")
            line = ""
        elif i == len(text) - 1:
            line += text[i]
            print(line)
            line = ""
        else:
            line += text[i]
