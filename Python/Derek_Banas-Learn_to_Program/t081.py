#!/usr/bin/python3

import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more\n")

with open("mydata.txt", encoding="utf-8") as myFile:
    lineNum = 1

    while (True):
        line = myFile.readline()

        if (not line):
            break

        print("Line", lineNum, ": ", line, end="")
        lineNum += 1
