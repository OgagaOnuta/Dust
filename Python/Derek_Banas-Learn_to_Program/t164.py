#!/usr/bin/python3

'''
SUBEXPRESSIONS are part of a larger expression,
and are surrounded with parentheses
'''

import re

randStr = "My number is 412-555-1212"

regex1 = re.compile(r"412-(.*)")
regex2 = re.compile(r"412-(.*)-(.*)")

matches1 = re.findall(regex1, randStr)
matches2 = re.findall(regex2, randStr)

print(len(matches1))
for i in matches1:
    print(i)

print()
# print(matches2[0][0])
# print(matches2[0][1])

for i in matches2:
    print(i[0])
    print(i[1])
