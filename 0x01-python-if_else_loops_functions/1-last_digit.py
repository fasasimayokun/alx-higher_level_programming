#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    dig = -((-1 * number) % 10)
else:
    dig = number % 10

if dig == 0:
    print(f"Last digit of {number:d} is {dig:d} and is 0")
elif dig < 6 and dig != 0:
    print(f"Last digit of {number:d} is {dig:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {dig:d} and is greater than 5")
