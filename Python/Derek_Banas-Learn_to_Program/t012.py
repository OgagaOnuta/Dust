#!/usr/bin/python3

'''
The eval() function converts input to the required format

and: If both are true, return true
or: If either is true, return true
not: Convert a true condition to false and vice versa
'''
# We'll provide different output based on age
# 1 - 18 -> Important
# 21, 50, > 65 -> Important
# All others -> Not Important

# Receive age and store in age
age = eval(input("Enter age: "))

# if age is greater than or equal to 1 and less than or equal to 18, Important
if (age >= 1) and (age <= 18):
    print("Important Birthday")

# if age is either 21 or 50, Important
elif (age == 21) or (age == 50):
    print("Important Birthday")

# We check if age is less than 65 and then convert true to false and vice versa
elif not (age < 65):
    print("Important Birthday")

# Not Important
else:
    print("Sorry, Not Important")
