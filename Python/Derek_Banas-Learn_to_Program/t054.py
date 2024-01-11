#!/usr/bin/python3

'''
"*args" is used when we don't know the number of arguments
'''


def sumAll(*args):
    sum = 0

    for i in args:
        sum += i

    return (sum)


print("Sum: ", sumAll(1, 2, 3, 4, 5))
