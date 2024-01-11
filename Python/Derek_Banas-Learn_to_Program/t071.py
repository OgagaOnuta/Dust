#!/usr/bin/python3

'''
A Recursive Function is a function that refers to itself
i.e. it calls itself inside of itself

Every recursive function must contain a condition in which
it stops calling itself
'''


def factorial(num):
    if (num <= 1):
        return (1)
    else:
        result = num * factorial(num - 1)
        return (result)


print("4! =", factorial(4))
