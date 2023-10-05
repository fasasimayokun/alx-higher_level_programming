#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_c = len(sys.argv) - 1

    if arg_c == 0:
        print("0 arguments.")
    elif arg_c == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_c))

    for num in range(arg_c):
        print("{}: {}".format(num + 1, sys.argv[num + 1]))
