#!/usr/bin/python3
'''List Comprehension'''

listTable = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)
        if (j < 9):
            print(listTable[i][j], end=" || ")
        else:
            print(listTable[i][j])
