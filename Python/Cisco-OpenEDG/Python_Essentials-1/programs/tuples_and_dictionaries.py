'''
Tuples and dictionaries can work together
'''

# Bob: 7, 2, 9
# Andy: 3, 10, 3

# Create an empty dictionary for the input data
# where the student's name is the key, and the score (a tuple) is the value
school_class = {}

# Enter an infinite loop
while (True):
	# Read the student's name
	name = input("Enter the student's name: ")
	# Leave the loop if the name is empty
	if (name == ""):
		break

	# Ask for one of the student's scores
	score = int(input("Enter the student's score (0-10): "))
	# Leave the loop if the score entered is not within range
	if (score not in range(0, 11)):
		break

	# Lengthen the associated tuple if the student's name is already available
	if (name in school_class):
		school_class[name] += (score,)
	# Create a new entry if this is a new student (unknown to the dictionary)
	else:
		school_class[name] = (score,)

# Iterate through the sorted students
for name in sorted(school_class.keys()):
	# Initialize the data needed to evaluate the average
	adding = 0
	counter = 0

	# Iterate through the tuple and update the sum and counter
	for score in school_class[name]:
		adding += score
		counter += 1
	
	# Evaluate and print the student's name and average score
	print(name, ":", (adding / counter))
