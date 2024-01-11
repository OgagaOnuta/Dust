#!/usr/bin/python3

import random

listTable = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(10):
    for j in range(10):
        print(listTable[i][j], end="")
        if (j < 9):
            print(" || ", end="")
    print()
