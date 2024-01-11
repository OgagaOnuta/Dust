#!/usr/bin/python3

'''
EXCEPTIONS are going to be triggered either when an error
occurs or when you want an exception to be triggered.

Exceptions are used to handle errors, or to execute
specific code when something happens.

`else` is used when you want some code to run if an
exception does not occur
`finally` will be used when you want some code to
execute whether an exception is raised or not
'''


try:
    aList = [1, 2, 3]

    print(aList[3])
except (IndexError):
    print("Sorry, that index doesn't exist")
except (Exception):
    print("An unknown error occured")


class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dogName = input("What is your dog's name? ")

    if any(char.isdigit() for char in dogName):
        raise DogNameError
except DogNameError:
    print("Your dog's name can't contain a number")

print()

num1, num2 = input("Enter 2 values to divide: ").split()

try:
    quotient = int(num1) / int(num2)

    print("{} / {} = {}".format(num1, num2, quotient))
except (ZeroDivisionError):
    print("You can't divide by zero")
else:
    print("You didn't raise an exception")
finally:
    print("I execute no matter what")
