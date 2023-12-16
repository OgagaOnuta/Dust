'''
The Digit of Life
'''

# Ask user for their DOB in number format
dob = input("Enter your date of birth (YYYYMMDD): ")

# Iterate through string
while (True):
	# Create variable to store sum
	sum = 0
	
	# Add all numbers in the string
	for i in dob:
		sum += int(i)

	# Check the length of the sum
	if (len(str(sum)) == 1):
		break
	else:
		dob = str(sum)

# Print "The Digit of Life"
print(sum)
