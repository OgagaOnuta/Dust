'''
Reading ints safely

* accept three arguments:
	* a prompt
	* a low acceptible limit
	* and a high acceptable limit
'''


from typing import Type


def read_int(prompt, min, max):
	# Enter loop
	while (True):
		try:
			# Receive input
			value = int(input(prompt))
			# If input is valid, return input
			if (value in range(min, (max + 1))):
				return (value)
			else:
				raise Exception
		# If input is not int, repeat the loop
		except (ValueError):
			print("Error: wrong input")
		# If input is not within range, repeat loop
		except (Exception):
			print("Error: the value is not within permitted range ({}..{})".
		 			format(min, max))


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
