#!/usr/bin/python3

import re

randStr = "12345 12345-1234 1234 12346-333"
# Match 5 digit codes or 5 digits with a hyphen, then 4 digits
regex = re.compile(r"(\d{5}|\d{5}-\d{4})\s")
matches = re.findall(regex, randStr)

for i in matches:
    print(i)
