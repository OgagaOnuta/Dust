'''
A leap year: writing your own functions
'''

# Leap Year: divisible by 4 and not divisible by 100
# Leap Year: divisible by 4 and divisible by 100 and divisible by 400


def is_year_leap(year):
	# Check if divisible by 4
	if (year % 4 == 0):
		print("Year is divisible by 4")
		# Check if divisible by 100
		if (year % 100 == 0):
			print("Year is divisible by 100")
			# Check if divisible by 400
			if (year % 400 == 0):
				print("Year is divisible by 400")
				print("LEAP YEAR")
				return (True)
			else:
				print("Year is divisible by 4, 100, but not 400")
				print("COMMON YEAR")
				return (False)
		else:
			print("Year is not divisible by 100")
			print("LEAR YEAR")
			return (True)
	else:
		print("Year is not divisible by 4")
		print("COMMON YEAR")
		return (False)


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]

	print(yr, "-> ", end="")

	result = is_year_leap(yr)

	if (result == test_results[i]):
		print("OK")
	else:
		print("Failed")
