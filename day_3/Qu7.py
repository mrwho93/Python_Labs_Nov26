#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO preserve one python object
# to a pickle file using the pickle module

import sys
import re

if sys.platform == "win32":
    file=r"C:\WINDOWS\system32\drivers\etc\services"
else:
    file=r"/etc/services"


all_ports = set(range(1,201))
used_ports = set()

with open (file , mode='rt') as fh_in:
    for line in fh_in:
        match=re.search(r'(\d+)/(udp|tcp)', line)
     

        if match:
            match2 = match.group(2)
            print(match2)
        #if match:
        #    print(match)
            
            
#            if port <= 200:
               # used_ports.add(port)
#print(f"All ports={all_ports}")
#print(f"Used ports={used_ports}")
#print(f"Unsed ports={all_ports - used_ports}")
