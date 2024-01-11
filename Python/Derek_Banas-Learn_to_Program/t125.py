#!/usr/bin/python3

'''
`reduce` will receive a list and return a single result.
To use `reduce`, we would need to import it.
'''

from functools import reduce

print(reduce((lambda x, y: x + y), range(1, 6)))
