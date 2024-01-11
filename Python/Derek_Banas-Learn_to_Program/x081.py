#!/usr/bin/python3

import os

'''
Cycle through each line
Output the number of words per line and the average word length
'''

dirFiles = os.listdir()

for i in dirFiles:
    print(i)

print()
file = input("What file do you want to read? ")
print()

with open(file, encoding="utf-8") as myFile:
    lineNum = 1

    while (True):
        # Loop through each line
        line = myFile.readline()

        if (not line):
            break
        if (line == "\n"):
            lineNum += 1
            continue

        lineList = line.split()

        # Create variable to store number of words and length
        numWords = len(lineList)
        lengthOfWords = 0

        for i in lineList:
            lengthOfWords += len(i)

        # Calculate average length
        lengthAve = lengthOfWords / numWords

        # Output number of words and average word length
        print("Line", lineNum, ":")
        print("\tNumber of Words:", numWords)
        print("\tAverage Word Length: {:.2}".format(lengthAve))

        lineNum += 1
