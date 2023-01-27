#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = 0

    try:
        arg1, arg2 = args
        res = fct(arg1, arg2)
        return res
    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return None
