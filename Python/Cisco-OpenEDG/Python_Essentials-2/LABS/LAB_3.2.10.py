'''
Queue aka FIFO (First In - First Out): part 2
'''


class QueueError(LookupError):
	def __init__(self):
		LookupError.__init__(self)


class Queue:
	def __init__(self):
		self.queue_list = []

	def put(self, elem):
		self.queue_list.insert(0, elem)

	def get(self):
		if (len(self.queue_list) == 0):
			raise QueueError
		else:
			val = self.queue_list[-1]
			del self.queue_list[-1]
			return (val)


class SuperQueue(Queue):
	def __init__(self):
		Queue.__init__(self)

	def isempty(self):
		if (len(self.queue_list) == 0):
			return (True)
		else:
			return (False)


que = SuperQueue()

que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
	if (not que.isempty()):
		print(que.get())
	else:
		print("Queue empty")
