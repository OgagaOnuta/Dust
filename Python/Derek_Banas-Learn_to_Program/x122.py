#!/usr/bin/python3

'''
Find the multiples of 9 from a random 100 values list
with values between 1 and 1000
'''

import random

# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values
randList = list(random.randint(1, 1001) for i in range(100))

# Use modulus to find multiples of 9
print(list(filter((lambda x: x % 9 == 0), randList)))
