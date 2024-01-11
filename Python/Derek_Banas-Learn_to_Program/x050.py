#!/usr/bin/python3

'''
Solve for x
x + 4 = 9

x will always be the 1st value received and
you will only deal with the addition

Create a function that will
* Receive the string and split the string into variables
* Convert the strings into ints
* Convert the result into a string and join it to the string "x = ?"

Then a "print()" statement calling the function
'''


def xSolve():
    equation = input("Enter equation: ")
    x, operator, y, equal, z = equation.split()

    # Set val1
    if (x == "x"):
        val1 = int(y)
    elif (y == "x"):
        val1 = int(x)

    val2 = int(z)

    # Check the operator
    if (operator == "+"):
        result = val2 - val1
    elif (operator == "-"):
        if (y == "x"):
            result = val1 - val2
        else:
            result = val2 + val1
    elif (operator == "*"):
        result = val2 / val1
    elif (operator == "/"):
        if (y == "x"):
            result = val1 / val2
        else:
            result = val2 * val1

    return ("x = {}".format(result))


print(xSolve())
