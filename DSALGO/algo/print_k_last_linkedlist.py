

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

global index
index = 0
def printLastElements(node, k):
	global index
	if node != None:
		printLastElements(node.next, k)
		if index < k:
			print(node.data)
			index += 1


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)


printLastElements(head, 2)