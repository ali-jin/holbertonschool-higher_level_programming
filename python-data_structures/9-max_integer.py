#!/usr/bin/python3


def max_integer(my_list=[]):

    maxNum = my_list[0]
    if my_list == []:
        return None
    for i in range(1, len(my_list)):
        if my_list[i] > maxNum:
            maxNum = my_list[i]
    return maxNum
