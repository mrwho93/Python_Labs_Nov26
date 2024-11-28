#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo a safer way of managing file handles
# using a context resource manager (with statement). Simulating BLOCK scope.
"""
  Docstring
"""



movies = {'chris': ["die hard","trainspotting","barbie"],
          'tom': ["12 strong","forrest gump","the matrix"],
          'andrius': ["gladiator","the boondock saints","con air"],
          'winson': ["top gun","terminator","pretty women"]
         }

# Open file handle for WRITTING in TEXT mode
with open (r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.txt", mode="wt") as fh_out:
# ITERATE through movies dict and WRITE movie info to file handle
    for name in movies.keys():
        print (f"{name}: {movies[name]}", end="\n")
        print (f"{name} {(movies[name])}",end="\n", file=fh_out)


print("-"*100)
with open(r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.txt", mode="rt")as fh_in:
    for line in fh_in:
        print(line, end="")
