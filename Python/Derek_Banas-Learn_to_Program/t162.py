#!/usr/bin/python3

'''
We use "WORD BOUNDARIES" to decide where our matches both start and end.
This is represented by the "\b"
'''

import re

randStr = "ape at the apex"

regex = re.compile(r"\bape\b")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)
