'''
Collatz's hypothesis
'''

# Receive input from user
c0 = int(input("Enter a non-negative and non-zero number: "))

# Initialize steps
steps = 0

# Begin loop if c0 is not equal to 1
while (c0 != 1):
	# If c0 is even, c0 becomes (c0 // 2)
	# increase step by 1, output the value of the new c0
	# If c0 is odd, c0 becomes ((3 * c0) + 1)
	# increase step by 1, output the value of the new c0
	if (c0 % 2 == 0):
		c0 //= 2
		steps += 1
		print(c0)
	else:
		c0 = (3 * c0) + 1
		steps += 1
		print(c0)

print("steps =", steps)
