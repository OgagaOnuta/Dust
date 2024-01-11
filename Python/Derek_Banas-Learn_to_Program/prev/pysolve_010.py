#!/usr/bin/python3

'''
Problem : Receive miles and convert to kilometers
kilometers = miles * 1.60934
Enter Miles 5
5 miles equals 8.04 kilometers
'''
# Ask the user for input
miles = input('Enter Miles: ')

# Convert from string to integer
miles = int(miles)

# Convert to miles to kilometers
kilometers = miles * 1.60934

# Print expected output
print("{} miles equals {} kilometers".format(miles, kilometers))
