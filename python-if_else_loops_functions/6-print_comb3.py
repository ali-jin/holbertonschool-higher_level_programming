#!/usr/bin/python3

for i in range(100):
    for j in range(i, 10):
        if (i != j and i != 8):
            print("{}{}".format(i, j), end=", ")
print(89)
