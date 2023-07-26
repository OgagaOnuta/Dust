#!/usr/bin/python3

'''
If age is 5, Go to Kindergarten
Ages 6 through 17 goes to grades 1 through 12
If age is greater than 17, go to college
Try to complete with 10 or less lines
'''

# Receive age from user as input
age = eval(input("Enter age: "))

# Group age based on given conditions
if (age == 5):
    print("Go to Kindergarten")
elif (age >= 6 and age <= 17):
    grade = age - 5
    print("Go to Grade {}".format(grade))
elif (age > 17):
    print("Go to College")
else:
    print("Wait until you're 5 years old")
