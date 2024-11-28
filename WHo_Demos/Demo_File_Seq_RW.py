#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO open and read, write, and append, and close
# a TEXT file
 
"""
  Docstring
"""

movies = {'chris': ["die hard","trainspotting","barbie"],
          'tom': ["12 strong","forrest gump","the matrix"],
          'andrius': ["gladiator","the boondock saints","con air"],
          'winson': ["top gun","terminator","pretty women"]
         }

# Open file handle for WRITTING in TEXT mode
fh_out = open(r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.txt", mode="wt")


# ITERATE through movies dict and WRITE movie info to file handle

for name in movies.keys():
    print (f"{name}: {movies[name]}", end="\n")
    fh_out.write(f"{name} {(movies[name])}\n")



fh_out.close()

fh_in = open(r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.txt", mode="rt")


for line in fh_in:
    print(line, end="")






# print("-"*100)

# text = fh_in.read(30)
# text = fh_in.readlines()
# print(text[0])