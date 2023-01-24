#!/usr/bin/python3


def search_replace(my_list, search, replace):
    copyList = my_list.copy()

    for i in range(len(my_list)):
        if copyList[i] == search:
            copyList[i] = replace

    return copyList
