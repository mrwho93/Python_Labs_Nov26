#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO match text data using str testing
# and regular Expressions/Regex and the re module

import re


postcode = open(r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\labs\postcodes.txt", mode="rt")

valid = 0
invalid = 0

for line in postcode:
    if line.isspace(): continue
    line = line.upper()
    line = re.sub(r"\s+",r"", line) 
    line = re.sub(r"(\d[A-Z]{2})$",r" \1",line)

    m = re.search(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z]{2}$", line)
    if m:
        valid +=1
        print(line)
    else:
        invalid +=1
            
print({valid})
print({invalid})



    







