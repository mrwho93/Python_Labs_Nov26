#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo how to display the entire 
# unicode characterset

"""
  Docstring
"""

import sys

# Iterate through all the character position in unicode characterset

for pos in range (0, 0xffff):
    try:

        print(chr(pos), end="")
        if pos % 128 == 0:
            print()

    except UnicodeDecodeError:
        print(" ")
sys.exit(0)