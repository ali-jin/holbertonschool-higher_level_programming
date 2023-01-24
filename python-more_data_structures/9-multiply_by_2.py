#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    copyDict = a_dictionary.copy()
    keys = list(copyDict.keys())

    for k in keys:
        val = copyDict[k]
        copyDict[k] = val * 2

    return copyDict
