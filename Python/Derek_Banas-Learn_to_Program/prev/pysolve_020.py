#!/usr/bin/python3

'''
Have the user enter their investment amount and expected interest
Each year, their investment will increase by their
investment + their investment * interest rate
Print out the earnings after n year period
'''

# Receive investment and interest inputs from user
investment = input("Investment Amount: ")
interest = input("Interest Rate: ")

# Convert values to float
investment = float(investment)
interest = float(interest) * .01

# Cycle through years using a for loop
n = int(input("How many year(s) period: "))
for i in range(n):
    investment = investment + (investment * interest)

# Print out earnings
print("Current investment: {:.2f}".format(investment))
