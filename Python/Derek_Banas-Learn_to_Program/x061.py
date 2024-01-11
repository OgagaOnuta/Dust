#!/usr/bin/python3

'''
Generate a multiplication table
'''

# Create a 2-dimensional table from values 1 to 0
multTable = [[1] * 12 for i in range(10)]
for i in multTable:
    print(i)
print()

# Loop through and multiply the values in each cell
for i in range(10):
    for j in range(12):
        multTable[i][j] = (i + 1) * (j + 1)
        print("{:5d}".format(multTable[i][j]), end="")
        if (j < 11):
            print(" | ", end="")
    print()
