#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None

    keys = list(a_dictionary.keys())
    score = 0

    for k in keys:
        temp = a_dictionary[k]
        if temp > score:
            score = temp
            name = k

    return name
