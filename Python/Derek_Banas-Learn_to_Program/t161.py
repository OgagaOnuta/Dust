#!/usr/bin/python3

'''
Greedy match: Searches for the biggest match possible
Lazy match: Searches for the smallest match possible

We can make a greedy match lazy by adding the question mark (?) after it.
'''

import re

randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

regex1 = re.compile("<name>.*</name>")  # Greedy match
regex2 = re.compile("<name>.*?</name>")  # Lazy match
regex3 = re.compile("<name>(.*?)</name>")  # Subexpressions

matches1 = re.findall(regex1, randStr)
matches2 = re.findall(regex2, randStr)
matches3 = re.findall(regex3, randStr)

for i in matches1:
    print(i)
print()

for i in matches2:
    print(i)
print()

for i in matches3:
    print(i)
print()
