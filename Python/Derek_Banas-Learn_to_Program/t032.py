#!/usr/bin/python3

'''
methods can be accessed without referencing
the module when using the "from" statement
'''

from decimal import Decimal as D

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("Sum = ", sum)
print(".1 + .1 + .1 - .3 = ", (.1 + .1 + .1 - .3))
