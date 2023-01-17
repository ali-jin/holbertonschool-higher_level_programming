#!/usr/bin/python3

def uppercase(str):
    up = 0
    ch = ""
    for c in str:
        if ord(c) in range(97, 123):
            up = ord(c) - 32
            c = chr(up)
        ch += c
    print(ch)
    return ch
