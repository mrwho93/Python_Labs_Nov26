#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo how to Test which platform you
# are running on and will get the Home path of the user

import sys
import os
import platform

if sys.platform == "win32":
    home = os.environ["HOMEPATH"]
else:
    home = os.environ["HOME"]
print("My home directory is",home) 

print(platform.machine())
print(platform.architecture())
print(platform.node())
print(platform.python_implementation())