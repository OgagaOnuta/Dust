#!/usr/bin/python3

'''
Search for legitimate email addresses
'''

import re

randStr = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
regex = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
matches = re.findall(regex, randStr)

for i in matches:
    print(i)
