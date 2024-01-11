'''
How many days: writing and using your own functions
'''


def is_year_leap(year):
	if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
		return (True)
	else:
		return (False)
	

def days_in_month(year, month):
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	if ((year > 1582) and (month in range(1, 13))):
		if (is_year_leap(year)):
			month_days[1] = 29

		days = month_days[month - 1]

		return (days)


test_years = [1900, 2000, 2016, 1987, 1989]
test_months = [2, 2, 1, 11, 13]
test_results = [28, 29, 31, 30, None]

for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]

	print(yr, mo, "-> ", end="")

	result = days_in_month(yr, mo)

	if (result == test_results[i]):
		print("OK")
	else:
		print("Failed")
