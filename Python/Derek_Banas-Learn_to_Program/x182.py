#!/usr/bin/python3

'''
Match for different types of phone numbers
'''

import re

randStr = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
regex = re.compile(r"\d{10,11}|\(\d{3}\)\d+|\d{3}\s\d{3}\s\d{4}|\d{3}-\d{3}-\d{4}|\d{1}-\d{3}-\d{3}-\d{4}")
matches = re.findall(regex, randStr)

for i in matches:
    print(i)
