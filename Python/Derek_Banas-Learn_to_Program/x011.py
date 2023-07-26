#!/usr/bin/python3

# If age is 5, Go to Kindergarten
# Ages 6 through 17 goes to grades 1 through 12
# If age is greater than 17, go to College
# Complete with 10 or less lines

# Collect age as input
age = eval(input("Enter age: "))

# Check age and put in required grade
if (age == 5):
    print("Go to Kindergarten")
elif (age > 5) and (age <= 17):
    print("Go to grade {}".format(age - 5))
elif (age > 17):
    print("Go to College")
else:
    print("Wait until you're 5 years old")
