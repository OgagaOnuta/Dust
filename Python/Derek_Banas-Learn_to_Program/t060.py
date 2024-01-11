#!/usr/bin/python3

'''
Lists allow us to refer to a group of data using just one name
The first item in a list has an index of zero "0"
'''

import random
import math

randList = ["string", 1.234, 28]
oneToTen = list(range(10))
randList = randList + oneToTen

print(randList[0])
print("List Length: ", len(randList))

first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i), i))

print("string" in first3)
print("Index of string:", first3.index("string"))
print("How many strings:", first3.count("string"))
first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

first3.append("Another")

for i in first3:
    print("{} : {}".format(first3.index(i), i))
