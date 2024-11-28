#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO match text data using str testing
# and regular Expressions/Regex and the re module

import re

fh_in = open(r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\labs\words", mode="rt")


reobj = re.compile(r"^(.)(.).\2\1$")
# Iterate through the file handle one line at a time...

for line in fh_in:
    m = reobj.search(line)
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
