#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, (len(sys.argv))):
            print("{}:".format(i),  sys.argv[i])
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}:".format(1),  sys.argv[1])
    else:
        print("{} argument.".format(len(sys.argv) - 1))