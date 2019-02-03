class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, node):
		self.head = node
		self.tail = node

	def addNode(self, node):
		self.tail.next = node
		self.tail = node

	def __repr__(self):
		output = ""
		head = self.head
		while head is not None:
			output += str(head.data) + " -> "
			head = head.next
		output += "Null"
		return output

ll1 = LinkedList(Node(5))
duplicate = Node(11)
ll1.addNode(Node(14))
ll1.addNode(duplicate)
ll1.addNode(Node(55))
ll1.addNode(Node(66))
ll1.addNode(duplicate)
print(ll1)