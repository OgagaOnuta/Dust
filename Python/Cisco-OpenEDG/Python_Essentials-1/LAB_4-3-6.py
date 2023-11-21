'''
Day of the year: writing and using your own functions
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


def day_of_year(year, month, day):
	# Check condition for year and month
	if ((year > 1582) and (month in range(1, 13))):
		days = days_in_month(year, month)

		# Check condition for day
		if (day in range(1, (days + 1))):
			# Create variable to store the sum of days with the initial value of 0
			no_of_days = 0

			# Iterate through months (range(1, month))
			for i in range(1, month):
				# sum the days in month
				no_of_days += days_in_month(year, i)
	
			# Finally, add the day variable to the sum
			no_of_days += day

			return (no_of_days)


print(day_of_year(2000, 12, 31))
print()

test_years = [1900, 2000, 2016, 1987, 1989]
test_months = [2, 2, 1, 11, 13]
test_days = [20, 29, 15, 31, 1]
test_results = [51, 60, 15, None, None]

for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	da = test_days[i]

	print(yr, mo, da, "-> ", end="")

	result = day_of_year(yr, mo, da)

	if (result == test_results[i]):
		print("OK")
	else:
		print("Failed")
