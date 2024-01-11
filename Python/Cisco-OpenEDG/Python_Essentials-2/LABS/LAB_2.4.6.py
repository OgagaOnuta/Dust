'''
A LED Display
'''

# L0 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
L1 = ["###", "#", "###", "###", "# #", "###", "###", "###", "###", "###"]
L2 = ["# #", "#", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #"]
L3 = ["# #", "#", "###", "###", "###", "###", "###", "  #", "###", "###"]
L4 = ["# #", "#", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #"]
L5 = ["###", "#", "###", "###", "  #", "###", "###", "  #", "###", "###"]

# Receive user input
user_input = input("Enter any non-negative number: ")

# Loop five times representing each layer
for i in range(1, 6):
	# Loop through the string for each iteration
	for digit in user_input:
		# Convert character to number
		num = int(digit)
		# Print the corresponding loop layer
		if (i == 1):
			print(L1[num], end=" ")
		elif (i == 2):
			print(L2[num], end=" ")
		elif (i == 3):
			print(L3[num], end=" ")
		elif (i == 4):
			print(L4[num], end=" ")
		elif (i == 5):
			print(L5[num], end=" ")

	# Print new line
	print()
