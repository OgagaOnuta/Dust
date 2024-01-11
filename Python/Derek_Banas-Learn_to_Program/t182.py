#!/usr/bin/python3

'''
Match Object Functions provide more information on your matches
'''

import re

match = re.search(r"\d{2}", "The chicken weighed 13 lbs")

print("Match:", match.group())
print("Span:", match.span())
print("Start:", match.start())
print("End:", match.end())
