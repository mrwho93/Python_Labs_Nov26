#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo

"""
  Docstring
"""

def get_numbers():
    """ Return an ENTIRE list of numbers """
    numbers = []
    for x in range (0,100):
        numbers.append(x)
    return numbers


def generate_numbers():
    """ Yield one object at a time from a collection of numbers """
    print("Executing generate_numbers...")
    for x in range(0,10):
        yield x


for z in get_numbers():
    print(z)



# Alternatively we could use a WHILE loop and the built in
# next() function to get the NEXT YIELDED value.

gen = generate_numbers()
while True:
    num = next(gen,-1)
    if num != -1:
        print(num)
    else:
        break


gen = generate_numbers()
num1 = next(gen)
print(num1)