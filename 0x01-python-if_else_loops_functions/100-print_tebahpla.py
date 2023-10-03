#!/usr/bin/python3

num = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ch - num)), end='')
    if num == 0:
        num = 32
    else:
        num = 0
