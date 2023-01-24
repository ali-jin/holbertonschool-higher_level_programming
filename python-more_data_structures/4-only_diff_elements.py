#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    newSet = []
    listSet1 = list(set_1)
    listSet2 = list(set_2)

    for i in range(len(set_1)):
        if listSet1[i] not in listSet2:
            newSet.append(listSet1[i])

    for j in range(len(set_2)):
        if listSet2[j] not in listSet1:
            newSet.append(listSet2[j])

    return set(newSet)
