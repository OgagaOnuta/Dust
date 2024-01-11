#!/usr/bin/python3

'''
--------------- PROBLEM ---------------
- Create a random list filled with characters
  H AND T for heads and tails
- Output the number of Hs and Ts

Example Output
==============
Heads: 46
Tails: 54
'''

import random

# Create the list
flipList = []

# Populate the list with 100 Hs and Ts
for i in range(1, 101):
    # flipList.append(random.choice(["H", "T"]))

    # Appending to a list using "+="
    flipList += random.choice(["H", "T"])

# Output the results
print("Heads:", flipList.count("H"))
print("Tails:", flipList.count("T"))
