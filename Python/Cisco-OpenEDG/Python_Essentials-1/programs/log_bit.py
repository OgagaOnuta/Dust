'''
Checking the difference between Logical and Bitwise Operators
'''

i = 15
j = 22

log = bool(i and j)
bit = int(bin(i), 2) & int(bin(j), 2)

logneg = not i
bitneg = ~int(bin(i), 2)

print(log, "\n", bit, "\n", logneg, "\n", bitneg, sep="")
