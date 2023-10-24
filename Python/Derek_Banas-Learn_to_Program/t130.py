#!/usr/bin/python3

'''
An ITERABLE is a stored sequence/list of values.
An Iterable will return an ITERATOR.
An Iterator will retrieve the next value from a sequence of values.
'''

# Convert string to iterable
sampStr = iter("Sample")

# Get the next character in the iterable
print("Char:", next(sampStr))
print("Char:", next(sampStr))
print()


class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    # ITERABLE
    def __iter__(self):
        return (self)

    # ITERATOR
    def __next__(self):
        if (self.index >= (len(self.letters) - 1)):
            raise (StopIteration)

        self.index += 1
        return (self.letters[self.index])


alpha = Alphabet()

for letter in alpha:
    print(letter)

print()

david = {"fName": "David", "lName": "Onuta"}

for key in david:
    print(key, ":", david[key])
