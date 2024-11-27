#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOW TO creat, grow, and shrink and access
# keys and values in a dictionary (Unordered collection with unique keys)
# Py3.6 onwards, keys are INSERTION order!
"""
  Docstring
"""
import pprint
movies = {'chris': ["die hard","trainspotting","barbie"],
          'tom': ["12 strong","forrest gump","the matrix"],
          'andrius': ["gladiator","the boondock saints","con air"],
          'winson': ["top gun","terminator","pretty women"]
         }

# Grow a dict

movies['naoki']=["titanic","star wars","spiderman"]
movies['donald']=["seven samurai","battle royale","the last samurai"]


# Access a dict

print(f"Chrisy's favorite movie are {movies['chris']}")

print(f"Tom's ultimate movies is {movies['tom'][0]}")

print(f"Andrius's best film is {movies.get('andrius')}")

#shrink a dict..

films = movies.copy() # Shallow Copy
films.clear() # Empty dict..
movies.pop('winson') # Pop/remove 'Winson' key_value
movies.popitem() # Removes LAST INSERTED key_value
pprint.pprint(movies) # Display sorted keys+values in human pretty format

print("-"*60)
# Accessing a dict and it's keys and values.
# 1. Using an ITERATOR loop 
for name in movies.keys():
    print(f"{name} likes {movies[name]}")
print("-"*60)
for films in movies.values():
    print(f"good films = {films}")
print("-"*60) 
for (name, films) in movies.items():
    print(f"{name} loves the films {films}")  