#!/usr/bin/python3

'''
Using a do...while loop,
Guess a number between 1 and 10,
and tell the user if they were right
'''

import random

num = random.randrange(1, 11)

while (True):
    user_num = int(input("Guess a number between 1 and 10: "))

    if (num == user_num):
        print("You guessed right")
        break
