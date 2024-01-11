#!/usr/bin/python3

'''
Back Reference allows us to reuse the expression that preceeds it
'''

import re

randStr = "the cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+\1")  # \1 represents the back reference
matches = re.findall(regex, randStr)

print("Matches:", len(matches))

for i in matches:
    print(i)

print()

# - - - - - - - - - - - - - - - - - - - -

randStr = "<a href='#'><b>The Link</b></a>"
regex = re.compile(r"<b>(.*?)</b>")
randStr = re.sub(regex, r"\1", randStr)

print(randStr)
print()

# - - - - - - - - - - - - - - - - - - - -

randStr = "412-555-1212"
regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
randStr = re.sub(regex, r"(\1)\2", randStr)  # first and second back reference

print(randStr)
