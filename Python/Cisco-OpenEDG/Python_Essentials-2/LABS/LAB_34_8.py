'''
Days of the week
'''


class WeekDayError(Exception):
	pass


class Weeker:
	__weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]	

	def __init__(self, day):
		if (day in Weeker.__weekday):
			self.__day = day
		else:
			raise WeekDayError

	def __str__(self):
		return (self.__day)

	def add_days(self, n):
		# Get index of __day in __weekday
		idx = Weeker.__weekday.index(self.__day)
		# Add n to the index
		new_idx = idx + n
		# Get the value of the sum modulo 7
		new_idx %= 7
		# Return the element at that index
		self.__day = Weeker.__weekday[new_idx]

	def subtract_days(self, n):
		# Reverse the __weekday list
		Weeker.__weekday.reverse()
		# Get index of __day in __weekday
		idx = Weeker.__weekday.index(self.__day)
		# Add n to the index
		new_idx = idx + n
		# Get the value of the sum modulo 7
		new_idx %= 7
		# Return the element at that index
		self.__day = Weeker.__weekday[new_idx]

		# # Get index of __day in __weekday
		# idx = Weeker.__weekday.index(self.__day)
		# # Subtract n from the index
		# new_idx = idx - n
		# # Get the value of the subraction modulo 7
		# new_idx %= 7
		# # Return the element at that index
		# self.__day = Weeker.__weekday[new_idx]


try:
	weekday = Weeker("Mon")
	print(weekday)
	weekday.add_days(15)
	print(weekday)
	weekday.subtract_days(23)
	print(weekday)
	weekday = Weeker("Monday")
except WeekDayError:
	print("Sorry, I can't serve your request.")
