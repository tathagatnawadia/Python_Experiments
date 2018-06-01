class LinkedList:
	def __init__(self, data):
		self.data = data
		self.next = None


a = LinkedList(3)
a.next = LinkedList(2)
a.next.next = LinkedList(3)
a.next.next.next = LinkedList(3)
a.next.next.next.next = LinkedList(10)
a.next.next.next.next.next = LinkedList(8)
a.next.next.next.next.next.next = LinkedList(3)
M = 3

original = a
start = None
prev = None

while a != None:
	if a.data == M:
		a = a.next
		continue
	if prev is None:
		start = a
		prev = a
	else:
		prev.next = a
		prev = a
	a = a.next

prev.next = None

while start != None:
	print(start.data)
	start = start.next