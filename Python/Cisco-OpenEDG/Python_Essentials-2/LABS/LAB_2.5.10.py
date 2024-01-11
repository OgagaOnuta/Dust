'''
Find a word!
'''

# Get first string (searching for)
word = input("Enter string to look for: ").lower()

# Get second string (searching in)
words = input("Enter string to search: ").lower()

# Variable to check if first is found in second
check = False

# Loop through first string
for char in word:
	# Check if character is in second string
	if (char in words):
		check = True
	else:
		check = False
		break

# Output result
if (check):
	print("Word found")
else:
	print("Word not found")
