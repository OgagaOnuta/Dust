<<<<<<< HEAD
'''
The Timer class
'''


class Timer:
	def __init__(self, hours = 0, minutes = 0, seconds = 0):
		self.__hours = hours
		self.__minutes = minutes
		self.__seconds = seconds

	def __str__(self):
		return ("{:02}:{:02}:{:02}".
		  format(str(self.__hours), 
		   str(self.__minutes), 
		   str(self.__seconds)))

	def next_second(self):
		self.__seconds += 1

		if (self.__seconds > 59):
			self.__seconds = 0
			self.__minutes += 1
			if (self.__minutes > 59):
				self.__minutes = 0
				self.__hours += 1
				if (self.__hours > 23):
					self.__hours = 0

	def prev_second(self):
		self.__seconds -= 1

		if (self.__seconds < 0):
			self.__seconds = 59
			self.__minutes -= 1
			if (self.__minutes < 0):
				self.__minutes = 59
				self.__hours -= 1
				if (self.__hours < 0):
					self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
=======
'''
The Timer class
'''


class Timer:
	def __init__(self, hours = 0, minutes = 0, seconds = 0):
		self.__hours = hours
		self.__minutes = minutes
		self.__seconds = seconds

	def __str__(self):
		return ("{:02}:{:02}:{:02}".
		  format(str(self.__hours), 
		   str(self.__minutes), 
		   str(self.__seconds)))

	def next_second(self):
		self.__seconds += 1

		if (self.__seconds > 59):
			self.__seconds = 0
			self.__minutes += 1
			if (self.__minutes > 59):
				self.__minutes = 0
				self.__hours += 1
				if (self.__hours > 23):
					self.__hours = 0

	def prev_second(self):
		self.__seconds -= 1

		if (self.__seconds < 0):
			self.__seconds = 59
			self.__minutes -= 1
			if (self.__minutes < 0):
				self.__minutes = 59
				self.__hours -= 1
				if (self.__hours < 0):
					self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
>>>>>>> a2d5da838507028f23a8e226d69dfb9a3309cf1a
