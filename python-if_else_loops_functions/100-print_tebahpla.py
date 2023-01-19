#!/usr/bin/python3

for i in range(122, 96, -1):
    if (i % 2 != 0):
        print("{}".format(chr(i).upper()), end="")
    else:
        print("{:c}".format(i), end="")
