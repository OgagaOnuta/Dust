#!/usr/bin/python3

'''
Variable names can contain alphabets, numbers, and underscores but can
only begin with an alphabet or underscore, and must not contain keywords

The split() function separates input by a delimiter
The int() function converts input to integers
'''

# This is a single-line comment in Python
'''
This is a multi-line
comment in Python
'''

# Ask the user to input their name and assign it to a variable named name
name = input("What is your name? ")

# Print out hello followed by the name they entered
print("Hello ", name, "\n")

# Ask the user to input 2 values and store them in variables num1 and num2
num1, num2 = input("Enter 2 numbers: ").split()

# Convert the strings into regular numbers (Integers)
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Substract values and store in difference
difference = num1 - num2

# Multiply the values and store in product
product = num1 * num2

# Divide the values and store in quotient
quotient = num1 / num2

# Use modulus on the values to find the remainder
remainder = num1 % num2

# Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
