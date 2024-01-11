#!/usr/bin/python3

'''
Have the user enter their investment amount and expected interest
Each year, their investment will increase by their investment
plus their investment * interest
Print out the earnings after a 10 year period
'''

investment = float(input("Investment amount: "))
interest = float(input("Interest rate: ")) / 100

for i in range(10):
    investment += (investment * interest)

print("Compound Interest after 10 years: {:.2f}".format(investment))
