#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO match text data using str testing
# and regular Expressions/Regex and the re module

import re

fh_in = open(r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\labs\words", mode="rt")

# Iterate through the file handle one line at a time...

for line in fh_in:
    # Example of string testing
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search("level",line) # match lines with "town" in the string
    # m = re.search("town$",line) # match lines ending with "town" in the string
    # m = re.search("^[a-z]",line) # match lines ending with "town" in the string
    # m = re.search("[0-9]",line) # match lines ending with "town" in the string
    # m = re.search("^[adrp]ing$",line) # match lines ending with "town" in the string
    # m = re.search("^...................$",line) # match lines ending with "town" in the string
    # m = re.search("[aeiou]{5,}",line) # match lines ending with "town" in the string
    # m = re.search("\.",line) # match lines ending with "town" in the string
    # m = re.search("^[A-Z].*[A-Z]$",line) # match lines ending with "town" in the string
    # m = re.search("^.{22}$",line) # match lines ending with "town" in the string
    # m = re.search(r"^(.)(.).\2\1$",line) # match lines ending with "town" in the string
    # m = re.search(r"^([A-Z]).*\1$",line) # match lines ending with "town" in the string
    m = re.fullmatch(r"^([A-Z]).*\1\n$",line) # match lines ending with "town" in the string
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}, "
              f"Groupings={m.group()}, Group 1= {m.group(1)}")






fh_in.close()

