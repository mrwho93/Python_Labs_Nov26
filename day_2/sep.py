#! /usr/bin/python
#                    1         2         3         4
#          012345678901234567890123456789012345678901234567890
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-" * len(Belgium))
print(Belgium.replace(",", ":"))

pop_country = int(Belgium[8:16]) # Remember to CONVERT str into int!
pop_capital = int(Belgium[26:32])

print(f"Population of Country and capital = {pop_country + pop_capital}")
print("-" * len(Belgium))



Length = len(Belgium)
print("Belgium string has a length of: ",Length)

print("-"*Length)
Belgium2 = Belgium.replace(",",":")

Belgium_population = Belgium[8:16]
Belgium_capital = Belgium[16:32]

Belgium_total = Belgium_capital.astype(int) + Belgium_population.astype(int)
print("The calculation total is: ", Belgium_total)

print(Belgium2)