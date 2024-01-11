#!/usr/bin/python3

import random

randList = []

for i in range(5):
    randList.append(random.randrange(1, 10))

randList.insert(5, 10)
print(randList)

randList.remove(10)
print(randList)

randList.pop(2)
print(randList)

randList.sort()
print(randList)

randList.reverse()
print(randList)
