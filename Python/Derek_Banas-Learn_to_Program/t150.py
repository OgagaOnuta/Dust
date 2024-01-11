#!/usr/bin/python3

'''
REGULAR EXPRESSIONS (REGEX)
They are used to:
- Search for a specific string in a large amount of data
- Verify that a string has the proper format (Email, Phone Number)
- Find a string and replace it with another string
- Format data into the proper form

===================================================================

- A period (.) is used to match any one character.
- A plus (+) is used to match one or more characters that preceeds it.
- A square bracket ([]) is used to match one or a range of any of
  several letters. The characters in the square brackets are case sensitive.
  Placing a caret (^) in the square brackets will search for characters not
  specified.
'''

import re  # Regular Expression

if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

print()
allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

print()
theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
    locTuple = i.span()

    print(locTuple)
    print(theStr[locTuple[0]:locTuple[1]])

print()
animalStr = "Cat rat mat pat"

allAnimals = re.findall("[crmfp]at", animalStr)

for i in allAnimals:
    print(i)

print()
someAnimals1 = re.findall("[c-mC-M]at", animalStr)
someAnimals2 = re.findall("[^Cr]at", animalStr)

for i in someAnimals1:
    print(i)

print()
for i in someAnimals2:
    print(i)

print()
print("Matches:", len(re.findall("a+", "a as ape bug")))
