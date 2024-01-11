#!/usr/bin/python3

r'''
\b : Backspace
\f : Form Feed
\r : Carriage Return
\t : Tab
\v : Vertical Tab

\d : [0-9]
\D : [^0-9]
\w : [a-zA-Z0-9_]
\W : [^a-zA-Z0-9_]
\s : [\f\n\r\t\v]
\S : [^\f\n\r\t\v]
'''

import re

owlFood = "rat cat mat pat"
regex = re.compile("[cr]at")
owlFood = regex.sub("owl", owlFood)

print(owlFood)
print()

randStr = "Here is \\stuff"

print("Find \\stuff:", re.search("\\stuff", randStr))
print("Find \\stuff:", re.search("\\\\stuff", randStr))

# Using rawstrings will not treat escape characters special
print("Find \\stuff:", re.search(r"\\stuff", randStr))
print()

randStr = "F.B.I. I.R.S. CIA"

print("Matches:", len(re.findall(r".\..\..\.", randStr)))
print()

randStr = '''This is a long
string that goes
on for many lines
'''

print(randStr)

regex = re.compile("\n")
randStr = regex.sub(" ", randStr)

print(randStr)
print()

randStr = "12345"

print("Matches:", len(re.findall(r"\d", randStr)))
print("Matches:", len(re.findall(r"\d{5}", randStr)))  # 5 digit figures
print("Matches:", len(re.findall(r"\d{2}", randStr)))  # 2 digit figures
print()

numStr = "123 12345 123456 1234567"

print("Matches:", len(re.findall(r"\d{5,7}", numStr)))  # 5 to 7 digit figures
print()

phNum = "412-555-1212"

if re.search(r"\w{3}-\w{3}-\w{4}", phNum):
    print("It is a phone number")

if re.search(r"\w{2,20}", "Ultraman"):
    print("Is a valid name")

if re.search(r"\w{2,20}\s\w{2,30}", "Toshio Muramatsu"):
    print("It is valid")
