#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo how to create, and grow, and shrink and
# combine sets using SET operator (rember VENN diagrams from school)

"""
  Docstring
"""

marvel_fans = {'donald','naoki','chris','isla','grace'}

dc_fans = set () # create and empty set

# Grow a set..

dc_fans.add('donald')
dc_fans.add('tom')
dc_fans.add('andrius')

# Shrink a set..

#dc_fans.pop() # Randomly remove a value.
comic_fans = dc_fans.copy()
comic_fans.clear()



print(f"Fans of Morvel = {marvel_fans}")
print(f"Fans of DC {dc_fans}")



# COMBINE sets using SET OPERATIONS (Remember VENN diagrams)


print(f"Fans of EITHER Marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of BOTH Marvel or DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel or DC = {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel or DC = {marvel_fans.symmetric_difference(dc_fans)}")

print("-"*50)
print(f"Fans of EITHER Marvel or DC = {marvel_fans | dc_fans}")
print(f"Fans of BOTH Marvel or DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel or DC = {marvel_fans - dc_fans}")
print(f"Fans of ONLY Marvel or DC = {marvel_fans ^ dc_fans}")