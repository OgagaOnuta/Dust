#!/usr/bin/python3

'''
Generate a random list of 5 values between 1 and 9
'''

import random

randList = []

for i in range(5):
    randList.append(random.randrange(1, 10))

print(randList)
