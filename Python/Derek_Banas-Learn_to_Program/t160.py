#!/usr/bin/python3

'''
- A question mark (?) matches zero or one of the character that preceeds it.
- An asterisk (*) matches zero or more of the character that preceeds it.
'''

import re

randStr1 = "cat cats"
randStr2 = "doctor doctors doctor's"

regex1 = re.compile("[cat]+s?")
regex2 = re.compile("[doctor]+['s]*")  # [doctr]+['s]* will also work

matches1 = re.findall(regex1, randStr1)
matches2 = re.findall(regex2, randStr2)

for i in matches1:
    print(i)

for i in matches2:
    print(i)
