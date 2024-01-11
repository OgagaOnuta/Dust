#!/usr/bin/python3

'''
Variables defined inside a function are available only to that function
and are known as "Local Variables"

"Global Variables" are variables defined outside of a function, and are
not necessarily going to change the value of the variable outside even
if passed inside a function
'''

# Defining a function


def add_numbers(num1, num2):
    return num1 + num2


print("5 + 4 =", add_numbers(5, 4))


def change_name(name):
    return "Mark"


name = "Tom"

name = change_name(name)

print(name)
