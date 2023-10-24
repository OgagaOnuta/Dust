#!/usr/bin/python3

'''
`map` allows us to execute a function on each item in a list
'''

oneTo10 = range(1, 11)


def dbl_num(num):
    return (num * 2)


# Coverting `map` result to a list
print(list(map(dbl_num, oneTo10)))
print(list(map((lambda x: x * 3), oneTo10)))

aList = list(map((lambda x, y: x + y), [1, 2, 3], [6, 7, 8]))

print(aList)
