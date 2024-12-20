#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo how to repeat a block of 
# commands a specific number of times using a counter loop.

count = 0 # 1. Initialise counter
while count < 10: #2. Test counter
    print(count)
    count += 1 #3. Increment counter


# Alternatively we could repeat block commands using a
# for loop and built in range (start, stop, step) function.

for num in range(0, 10, 1)
    print(num)