#!/usr/bin/python3

'''
FUNCTION ANNOTATION
====================
Defining the data types of attributes and return values.
They do not affect how the function operates, but mainly for documentation.
'''


def random_func(name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("Age: ", age)
    print("Weight: ", weight)

    return ("{} is {} years old and weighs {}".format(name, age, weight))


print(random_func("David", 26, 50.0))
print()

# Annotations are not strict rules
print(random_func(89, "David", "Turtle"))
print()

# Printing the annotations
print(random_func.__annotations__)
