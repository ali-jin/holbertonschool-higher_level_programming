#!/usr/bin/python3


def common_elements(set_1, set_2):
    newSet = []
    listSet1 = list(set_1)
    listSet2 = list(set_2)

    for i in range(len(set_1)):
        temp = listSet1[i]
        for j in range(len(set_2)):
            if listSet2[j] == temp and temp not in newSet:
                newSet.append(temp)

    return set(newSet)
