#!/usr/bin/python3

'''
ANONYMOUS FUNCTIONS using "lambda"
==================================
"lambda" functions can also be assigned to a name

`lambda arg1, arg2, ...: expression using the arguments`
'''

import random

# USE A `def` INSTEAD
# sum = lambda x, y: x + y

# print("4 + 5 =", sum(4, 5))
# print()

# USE A `def` INSTEAD
# can_vote = lambda age: True if age >= 18 else False

# print("Can 16 years vote?", can_vote(16))
# print("Can 19 years vote?", can_vote(19))
# print()

# Using lambda in a list
powerList = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

for func in powerList:
    print(func(4))

print()

# Storing lambda inside of a dictionary
attack = {"quick": (lambda: print("Quick Attack")),
          "power": (lambda: print("Power Attack")),
          "miss": (lambda: print("Missed Attack"))}

attack["quick"]()

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()
