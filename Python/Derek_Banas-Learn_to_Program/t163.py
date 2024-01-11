#!/usr/bin/python3

'''
STRING BOUNDARIES

^ : Beginning of the string
$ : End of the string
'''

import re

randStr1 = "Match everything up to @"
randStr2 = "@ Get this string"
randStr3 = '''Ape is big
Turtle is slow
Cheetah is fast
'''

regex1 = re.compile(r"^.*[^@]")
regex2 = re.compile(r"[^@\s].*$")
regex3 = re.compile(r"(?m)^.*?\s")  # Multi-line code (?m)

matches1 = re.findall(regex1, randStr1)
matches2 = re.findall(regex2, randStr2)
matches3 = re.findall(regex3, randStr3)

print(len(matches1))
for i in matches1:
    print(i)

print()

print(len(matches2))
for i in matches2:
    print(i)

print()

print(len(matches3))
for i in matches3:
    print(i)
