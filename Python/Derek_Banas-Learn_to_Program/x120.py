#!/usr/bin/python3

'''
- Create a function that receives a list and a function
- The function passed will return True or False if a list value is odd
- The surrounding function will return a list of odd numbers
'''


# Create outer function
def oddList(func, theList):
    # Create new list
    oddList = []

    # Loop through list items
    for i in theList:
        # If list item is odd, append to new list
        if (func(i) is True):
            oddList.append(i)

    # Return list of odd numbers
    return (oddList)


# Create function to check for even or odd numbers
def check_odd(num):
    # Return True if odd
    if ((num % 2) != 0):
        return (True)
    # Return False if even
    elif ((num % 2) == 0):
        return (False)


listed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(oddList(check_odd, listed))
