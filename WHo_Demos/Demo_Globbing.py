#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo how to iterate through files
# and the file system using a ITERATOR for loop plus the glob module.


import glob
import sys
import os


if sys.platform == "win32":
    if os.environ["HOMEPATH"]:
        home = os.environ["HOMEPATH"]
    else:
        home = r"C:\Users\who"
    pattern = home + "\*"
else:
    home = os.environ["HOME"]
    pattern = home + "/*"


print(pattern)
for file in glob.glob(pattern):
    if os.path.isfile(file):
        print(file, os.path.getsize(file))


