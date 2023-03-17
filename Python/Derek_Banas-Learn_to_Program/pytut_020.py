#!/usr/bin/python3

# Use for loop through the list from 1 to 21
for i in range(1, 21):

    # Use modulus to check that the result is NOT EQUAL to 0
    if ((i % 2) != 0):

        # Print the odds
        print("i = ", i)

your_float = input("Enter a float: ")
your_float = float(your_float)
print("Round to 2 decimals : {:.2f}".format(your_float))
