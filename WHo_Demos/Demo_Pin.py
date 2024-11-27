#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will simulate a high street bank PIN machine

import getpass

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = getpass.getpass("Enter PIN: ")
    if pin == master_pin:1
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # EXECUTES only ONCE when while condition become false   
    print("Too many attepts...")     
    print("Your cards has been retained. Have aa nice day")
print("Done")      