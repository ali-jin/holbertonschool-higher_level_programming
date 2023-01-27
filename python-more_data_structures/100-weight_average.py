#!/usr/bin/python3


def weight_average(my_list=[]):
    scores = 0
    weight = 0

    if my_list is None:
        return 0

    for tup in my_list:
        nb1, nb2 = tup
        scores += (nb1 * nb2)
        weight += nb2
    average_score = scores / weight

    return average_score
