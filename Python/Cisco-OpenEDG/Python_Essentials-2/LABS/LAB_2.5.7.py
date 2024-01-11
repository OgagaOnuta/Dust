'''
Palindromes
'''

# Ask user for some text
text = input("Enter text to check: ")

# Convert string to list
list_1 = []

for char in text:
	if (char == " "):
		continue

	list_1.append(char.lower())

check = True  # To check the characters
length = len(list_1)  # To store the list length

# Compare beginning indices to ending indices
for i in range(length):
	if ((length < 2) or (list_1[i] != list_1[length - 1 - i])):
		check = False
		break

if (check == True):
	print("It's a palindrome")
else:
	print("It's not a palindrome")
