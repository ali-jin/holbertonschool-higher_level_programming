#!/usr/bin/python3


def list_copy(my_list):
    copy = []
    for i in range(len(my_list)):
        copy.append(my_list[i])
    return copy


def new_in_list(my_list, idx, element):
    newList = list_copy(my_list)

    if idx < 0 or idx > len(my_list) - 1:
        return newList
    newList[idx] = element

    return newList
