#!/usr/bin/python3
'''List Comprehension'''

multTable = [[0] * 10 for i in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        multTable[i][j] = i * j
        print("{:2d}".format(multTable[i][j]), end="")
        if (j < 9):
            print(" | ", end="")
    print()
