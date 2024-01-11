#!/usr/bin/python3

'''
Receive a string
Hide its meaning by turning it into a string of unicode
Translate from unicode back to the original string
'''

# Receive input as string
user_input = str(input("Enter message: "))

# Create empty string to store encoded string
secret_msg = ""

# Loop through each character in the string
for char in user_input:

    # Convert each character to unicode and store as a string
    char_code = str(ord(char))

    # Check length of unicode character
    char_len = len(char_code)

    # If length is one, begin string with "00" and append to new string
    if (char_len == 1):
        char_msg = "00"
        char_msg += char_code
        secret_msg += char_msg

    # If length is two, begin string with "0" and append to new string
    elif (char_len == 2):
        char_msg = "0"
        char_msg += char_code
        secret_msg += char_msg

    # Concatenate unicode strings to form a new string
    else:
        secret_msg += char_code

# Output the encoded string
print("Secret Message: {}".format(secret_msg))

# Create empty string to store decoded string
msg = ""

msg_len = len(secret_msg)
# Loop through the encoded string with a step of 3
for code in range(0, (msg_len - 1), 3):

    # Convert each 3 digit string to integer
    char_int = secret_msg[code] + secret_msg[code + 1] + secret_msg[code + 2]
    char_int = int(char_int)
    # Convert integer to character and append to string
    msg += chr(char_int)

# Output the decoded string
print("Decoded message: {}".format(msg))
