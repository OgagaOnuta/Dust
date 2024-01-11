'''
Improving the Caesar cipher

* asks the user for one line of text to encrypt
* asks the user for a shift value (an integer number from the range 1...25)
* prints out the encoded text
'''

text = input("Enter message to encrypt: ")
cipher = ""

# Check if shift value is valid
while (True):
	try:
		shift_value = int(input("Enter shift value (1 - 25): "))

		if (shift_value in range(1, 26)):
			break
	except (Exception):
		continue

# Iterate through text
for char in text:
	# Check if character is an alphabet
	if (char.isalpha()):
		# Convert character to code point add shift value
		enc = ord(char) + shift_value

		# Start from a/A when character reaches z/Z
		if ((enc > ord("z")) and char.islower()):
			enc = ord("a") + (enc - ord("z") - 1)

		if ((enc > ord("Z")) and char.isupper()):
			enc = ord("A") + (enc - ord("Z") - 1)

		# Replace character with cipher
		char = chr(enc)

	# Convert code point to character and append to cipher
	cipher += char

# Print cipher
print(cipher)
