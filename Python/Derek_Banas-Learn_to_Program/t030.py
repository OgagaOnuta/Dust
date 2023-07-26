#!/usr/bin/python3

while (True):
    try:
        number = int(input("Please enter a number: "))
        break
    except (ValueError):
        print("You didn't enter a number")
    except (Exception):
        print("An unknown error occured")

print("Thank you entering a number")
