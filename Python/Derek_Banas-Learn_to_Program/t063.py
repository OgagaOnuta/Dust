#!/usr/bin/python3

'''
List comprehension is another way for us to construct lists
and perform an operation on each item in the list
'''

import random
import math

evenList = [i*2 for i in range(10)]

for i in evenList:
    print(i)
print()

numList = [1, 2, 3, 4, 5]

listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]

for i in listOfValues:
    print(i)
print()

multiDList = [["*"] * 10 for i in range(10)]
multiDList[0][1] = 10

for i in multiDList:
    print(i)
