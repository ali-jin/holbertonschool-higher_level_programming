#!/usr/bin/python3


def max_integer(my_list=[]):

    maxNum = 0
    if my_list is None:
        return None
    for i in range(len(my_list)):
        if my_list[i] > maxNum:
            maxNum = my_list[i]
    return maxNum
