#!/usr/bin/python3
"""
DOCUMENTATION
"""


def func(num1, num2):
    """ DOCUMENTATION """
    if ((isinstance(num1, int)) and (type(num1) is not float)):
        raise Exception("Please input a number")
    elif ((type(num2) is not int) and (type(num2) is not float)):
        raise Exception("Please input a number")
    return (num1 + num2)

a = input("Enter num1: ")
b = input("Enter num2: ")

print(func(a, b))
