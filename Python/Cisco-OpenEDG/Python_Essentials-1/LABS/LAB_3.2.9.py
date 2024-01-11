'''
The "break" statement - Stuck in a loop
'''

# Create while loop
while (True):
	# Request input
	user_entry = input("Type in a word: ")
	# Initiate break statement
	if (user_entry == "chupacabra"):
		break

print("You've successfully left the loop.")
