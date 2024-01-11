'''
Anagrams
'''

# Ask the user for inputs
text_1 = input("Enter first text: ").lower()
text_2 = input("Enter second text: ").lower()

list_1, list_2 = [], []

# Convert strings to lists
for char in text_1:
	if (char == " "):
		continue

	list_1.append(char)

for char in text_2:
	if (char == " "):
		continue

	list_2.append(char)

# Check the length of the inputs
# If not equal, not an anagram
if ((len(list_1) != len(list_2)) or (len(list_1) == 0) or (len(list_2) == 0)):
	print("Not anagrams")
else:
	length = len(list_1)

	# Iterate for the duration of the length of the string
	while (length != 0):
		# Check if character in one string is the other
		if (list_1[0] in list_2):
			# If in string, remove from both strings
			list_2.remove(list_1[0])
			list_1.remove(list_1[0])

			if ((len(list_1) == 0) and (len(list_2) == 0)):
				print("Anagrams")

		# If not, not an anagram
		else:
			print("Not anagrams")
			break

		length -= 1
