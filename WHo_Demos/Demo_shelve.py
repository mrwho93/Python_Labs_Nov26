#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo

"""
  Docstring
"""

import shelve

movies = {'chris': ["die hard","trainspotting","barbie"],
          'tom': ["12 strong","forrest gump","the matrix"],
          'andrius': ["gladiator","the boondock saints","con air"],
          'winson': ["top gun","terminator","pretty women"]
         }


tv_series = {'chris': ["walking dead","yellowstone"],
          'tom': ["breaking bad","the boys"],
          'andrius': ["outlander","dads army"],
         }

books = {'andrius': ["dummys guid to python"],
          'winson': ["bextreme ironing"],
         }

with shelve.open(r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"C:\Users\who\Project\Python_Labs_Nov26\Python_Labs_Nov26\WHo_Demos\media") as db:
    print(f"Chris's favourite movies are {db['movies']['chris']}")
    print(f"Toms's favourite tv_series is {db['tv_series']['tom'][0]}")
    print(f"Winson's favourite books are {db['books']['winson']}")