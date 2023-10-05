#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_c = len(sys.argv) - 1
    print("{} arguments.".format(arg_c))
    for num in range(arg_c):
        print("{}: {}".format(num + 1, sys.argv[num + 1]))
