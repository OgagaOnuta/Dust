#!/usr/bin/python3

# While loops are used when you don't know how many times you would loop

import random

rand_num = random.randrange(1, 51)

# The while loop counter should be defined before the loop
i = 1
while (i != rand_num):
    i += 1

print("The random value is: ", rand_num)

# "continue" stops executing and jumps back to the top of the loop
# "break" stops executing and jumps out of the loop

print()
i = 1
while (i <= 20):
    if ((i % 2) == 0):
        i += 1
        continue

    if (i == 15):
        break

    print("Odd: ", i)
    i += 1
