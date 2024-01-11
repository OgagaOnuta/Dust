#!/usr/bin/python3

'''
GENERATOR EXPRESSIONS look just like List Comprehension
but they return results one at a time.
They are surrounded by parentheses instead of square brackets.
'''

double = (x * 2 for x in range(10))

print("Double:", next(double))
print("Double:", next(double))
print("Double:", next(double))
print()

for num in double:
    print(num)
