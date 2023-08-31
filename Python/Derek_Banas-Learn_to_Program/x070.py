#!/usr/bin/python3

'''
Create an array of customer dictionaries

- Enter Customer (Yes/No): y
- Enter Customer Name: David Onuta
- Enter Customer (Yes/No): y
- Enter Customer Name: Gospel Obi
- Enter Customer (Yes/No): n

David Onuta
Gospel Obi
'''

# Create empty list to store customer dictionaries
custArray = []

# Create loop condition
customer = True

# Create infinite loop to query Manager
while (customer is True):
    # Query Manager
    query = input("Enter Customer (Yes/No)? ").lower()

    # Exit loop if NO
    if (query == "no" or query == "n"):
        customer = False

    # Input Customer Name if YES
    elif (query == "yes" or query == "y"):
        fName, lName = input("Enter Customer Name (First Last): ").split()
        custArray.append({"firstName": fName, "lastName": lName})

# Print Customer details
# print(custArray)  # In an array of dictionaries
for cust in custArray:
    print(cust["firstName"], cust["lastName"])
