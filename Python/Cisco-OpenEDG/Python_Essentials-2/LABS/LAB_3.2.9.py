'''
Queue aka FIFO (First In - First Out)
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


que = Queue()

que.put(1)
que.put("dog")
que.put(False)

try:
	for i in range(4):
		print(que.get())
except (Exception):
	print("Queue error")
