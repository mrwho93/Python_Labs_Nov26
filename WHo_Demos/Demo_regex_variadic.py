#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO define and call a VARIADIC function.

"""
App to search for REGEX batternsin text files
"""

import re

# Example of a VARIADIC function that allows variable num of parameters.

def search_pattern(pattern=r"^.{19}$", *files):
    lines=0
    for file in files:
        with open(file, mode="rt") as fh_in:
            for line in fh_in:
                m = re.search(pattern,line) # match lines ending with "town" in the string
                if m:
                    lines += 1
                    print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
    return lines


num_lines = search_pattern(r"^.{10}$",r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\words", 
                           r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\words2", 
                           r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\words3")
print(f"Matched {num_lines} lines")