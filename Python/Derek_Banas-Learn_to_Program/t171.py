#!/usr/bin/python3

'''
A "LOOK AHEAD" defines a pattern to match but does not return
(?=expression)

A "LOOK BEHIND" looks before the text to return but does not return
(?<=expression)

NEGATIVE LOOK AHEAD : (?!expression)
NEGATIVE LOOK BEHIND : (?<!expression)
'''

from functools import reduce
import re

randStr = "One two three four"
regex = re.compile(r"\w+(?=\b)")  # Look Ahead
matches = re.findall(regex, randStr)

for i in matches:
    print(i)

print()

# - - - - - - - - - - - - - - - - - - - -

randStr = "1. Bread 2. Apples 3. Lettuce"
regex = re.compile(r"(?<=\d.\s)\w+")  # Look Behind
matches = re.findall(regex, randStr)

for i in matches:
    print(i)

print()

# - - - - - - - - - - - - - - - - - - - -

randStr = "<h1>I'm Important</h1> <h1>So am I</h1>"
regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")  # Look Ahead & Look Behind
matches = re.findall(regex, randStr)

for i in matches:
    print(i)

print()

# - - - - - - - - - - - - - - - - - - - -

randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex = re.compile(r"(?<!\$)\d+")
matches = re.findall(regex, randStr)

print(len(matches))

matches = [int(i) for i in matches]

print("Total Items {}".format(reduce((lambda x, y: x + y), matches)))
