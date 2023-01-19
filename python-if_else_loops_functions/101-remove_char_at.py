#!/usr/bin/python3


def remove_char_at(str, n):
    strCopy = ""

    if len(str) < n or n < 0:
        return str

    for i in range(len(str)):
        if str[i] != str[n]:
            strCopy += str[i]
        if (str[i] == str[n] and n == 0):
            strCopy += " "
    return strCopy
