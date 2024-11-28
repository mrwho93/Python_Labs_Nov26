#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO open, close, read and write
# Randomly to a file using the .seek() and .tell() methods
"""
  Docstring
"""

# Open file handle for WRITTING in TEXT mode
with open (r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90,)
    text= fh_in.read(30)
    print(f"Text at position {fh_in.tell()}={text}")

    fh_in.seek(135,0)
    text= fh_in.read(30)
    print(f"Text at position {fh_in.tell()}={text}")

print("-"*90)

with open (r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.txt", mode="rb") as fh_in2:
    fh_in2.seek(-90,2)
    text= fh_in2.read(30)
    print(f"Text at position {fh_in2.tell()}={text}")

    fh_in2.seek(-60,1)
    text= fh_in2.read(30)
    print(f"Text at position {fh_in2.tell()}={text}")


print("-"*100)

