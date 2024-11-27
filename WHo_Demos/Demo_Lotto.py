#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will generate 6 unique random numbers
# numbers
import random
"""
lotto = []

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate =", num)
"""


lotto = set() # PYTHONIC solution.


while len(lotto)<6:
        num=random.randint(1,50)
        lotto.add(num)
print("Lotter numbers =", sorted(lotto))       

        


