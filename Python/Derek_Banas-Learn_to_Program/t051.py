#!/usr/bin/python3

'''
The "global" keyword says to use the global version of the variable

A function without a return value will return "None"
'''

gbl_name = "Sally"


def change_name():
    global gbl_name
    gbl_name = "Sammy"


change_name()

print(gbl_name)


def get_sum(num1, num2):
    sum = num1 + num2


print(get_sum(5, 4))
