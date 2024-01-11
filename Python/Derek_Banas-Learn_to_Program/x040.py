#!/usr/bin/python3

'''
Generate an Acronym for any given input
'''

# Collect input
input_str = input("Enter word(s): ")

# Create empty string for acronym
acrn = ""

# Store first letter in uppercase
acrn += input_str[0].upper()

# Get length of string
length_str = len(input_str)

# Loop through string
for i in range(length_str):
    # If character is whitespace
    if (input_str[i] == " "):
        # If the character after whitespace is a whitespace, skip
        if (input_str[i+1] == " "):
            i += 1
            continue

        # If the word after whitespace is "of", skip
        elif (input_str[i+1].lower() == "o") and \
             (input_str[i+2].lower() == "f") and \
             (input_str[i+3] == " "):
            i += 3
            continue

        # If the word after whitespace is "and", skip
        elif (input_str[i+1].lower() == "a") and \
             (input_str[i+2].lower() == "n") and \
             (input_str[i+3].lower() == "d") and \
             (input_str[i+4] == " "):
            i += 4
            continue

        # Store the  uppercase of the character after the whitespcae
        acrn += input_str[i+1].upper()

# Print Acronym
print(acrn)
