#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO preserve one python object
# to a pickle file using the pickle module
"""
  Docstring
"""
import pickle
import pprint
import gzip

movies = {'chris': ["die hard","trainspotting","barbie"],
          'tom': ["12 strong","forrest gump","the matrix"],
          'andrius': ["gladiator","the boondock saints","con air"],
          'winson': ["top gun","terminator","pretty women"]
         }


# Open file handle for WRITTING in binary mode
# with gzip.open (r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.pgz", mode="wb") as fh_out:
with gzip.open (r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.pgz", mode="wb") as fh_out:
    pickle.dump(movies, fh_out, protocol=5)
  

#with open (r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.p", mode="rb") as fh_in:
with gzip.open (r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)
    
  
print("-"*100)

pprint.pprint(movies)
  
pprint.pprint("-"*100)
pprint.pprint(films)

