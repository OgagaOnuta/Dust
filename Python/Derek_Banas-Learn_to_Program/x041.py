#!/usr/bin/python3

'''
Caesar's Cipher
'''

words = input("Enter word(s) to cipher: ")
key = int(input("Number of characters to shift (1 - 26): "))

# Word to store cipher
cipher = ""

# Loop through each character in string
for char in words:
    # Check if character is an alphabet
    if (char.isalpha()):
        # Convert character to unicode and and add key
        code = ord(char) + key

        # Check if uppercase
        if (char.isupper()):
            # If less than A, move forward 26 characters
            if (code < ord("A")):
                code += 26
            # If greater than Z, move backward 26 characters
            if (code > ord("Z")):
                code -= 26
        # Check if lowercase
        else:
            # If less than a, move forward 26 characters
            if (code < ord("a")):
                code += 26
            # If greater than z, move backward 26 characters
            if (code > ord("z")):
                code -= 26

        # Convert unicode back to character
        char = chr(code)
        # Append to new string
        cipher += char
    else:
        cipher += char

print()
# Print ciphered word
print("Encrypted message:", cipher)

decipher = ""
# Loop through each character in cipher
for char in cipher:
    # Check if character is an alphabet
    if (char.isalpha()):
        # Convert character to unicode and and subtract key
        code = ord(char) - key

        # Check if uppercase
        if (char.isupper()):
            # If less than A, move forward 26 characters
            if (code < ord("A")):
                code += 26
            # If greater than Z, move backward 26 characters
            if (code > ord("Z")):
                code -= 26
        # Check if lowercase
        else:
            # If less than a, move forward 26 characters
            if (code < ord("a")):
                code += 26
            # If greater than z, move backward 26 characters
            if (code > ord("z")):
                code -= 26

        # Convert unicode back to character
        char = chr(code)
        # Append to new string
        decipher += char
    else:
        decipher += char

# Print deciphered word
print("Decrypted message:", decipher)
