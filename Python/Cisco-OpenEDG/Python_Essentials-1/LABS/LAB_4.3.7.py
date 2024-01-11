'''
Prime numbers - how to find them
'''


def is_prime(num):
	print("Checking " + str(num))

	# CiscoEDG HINT => for i in range(2, int(1 + num ** 0.5)):
	# My Solution => for i in range(2, num):

	for i in range(2, int(1 + (num ** 0.5))):
		print("(" + str(num) + "%" + str(i) + ")", end=" ")
		if (num % i == 0):
			print("\nDivisible by " + str(i) + ", NOT A PRIME NUMBER")
			return (False)

	print("\nPRIME NUMBER")
	return (True)


for i in range(1, 20):
	print()
	if is_prime(i + 1):
		print(i + 1, end="\n")
print()
