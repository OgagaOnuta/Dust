'''
A leap year: writing your own functions
'''

# CiscoEDG Python Essentials 1 HINT

def is_year_leap(year):
	if (year % 4 != 0):
		print("Not divisible by 4", "Common year")
		return (False)
	elif (year % 100 != 0):
		print("Not divisible by 100", "Leap year")
		return (True)
	elif (year % 400 != 0):
		print("Not divisible by 400", "Common year")
		return (False)
	else:
		print("Divisible by 4, 100, and 400", "Leap year")
		return (True)


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
