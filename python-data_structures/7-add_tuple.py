#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    res = []
    a_list = list(tuple_a)
    if len(a_list) < 2:
        for i in range(len(a_list), 2):
            a_list.append(0)

    b_list = list(tuple_b)
    if len(b_list) < 2:
        for i in range(len(b_list), 2):
            b_list.append(0)

    res = [a_list[0] + b_list[0], a_list[1] + b_list[1]]
    Newtuple = tuple(res)

    return Newtuple
