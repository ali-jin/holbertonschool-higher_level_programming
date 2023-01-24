#!/usr/bin/python3


def uniq_add(my_list=[]):
    res = 0

    for i in range(len(my_list)):
        temp = my_list[i]
        idx = i
        for j in range(idx, len(my_list)):
            if my_list[j] == temp:
                my_list[j] = 0
        res += temp

    return res
