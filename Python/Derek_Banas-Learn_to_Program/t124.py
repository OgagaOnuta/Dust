#!/usr/bin/python3

'''
`filter` will select items from a list based off of a function
'''

# Converting `filter` results into a list
print(list(filter((lambda x: x % 2 == 0), range(1, 11))))
