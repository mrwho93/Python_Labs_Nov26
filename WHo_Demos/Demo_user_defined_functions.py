#! /usr/bin/env python3
# Author: WHo
# Version: 1.0
# Description: This script will demo HOWTO define , name, call and optionally pass
# parameters in and optionally return data from a user function.

"""
  Docstring
"""


def say_hello(greeting:str="ciao", recipient:str="amici"):
    message = f"{greeting} {recipient}"
    print (message)
    return None


say_hello("hello","my friends")
say_hello("konichiwa","tomodachi")
say_hello("bonjour","mes amis")
