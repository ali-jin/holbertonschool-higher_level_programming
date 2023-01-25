#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x - 1):
            print("{}".format(my_list[i]), end="")
            count += 1
        print("{}".format(my_list[i + 1]))
        return count + 1
    except:
        print("")
        return len(my_list)
