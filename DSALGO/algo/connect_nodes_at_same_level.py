class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		self.next = None


def printLevelOrder(root):
	queue = []
	queue.append(root)
	print(root.data)
	reverse = True
	while len(queue) != 0:
		curr_length = len(queue)

		while curr_length != 0:
			curr = queue.pop(0)
			if curr.left != None:
				queue.append(curr.left)
			if curr.right != None:
				queue.append(curr.right)
			curr_length -= 1

		for i in range(0, len(queue)-2):

		if reverse == True:

		else:
			
		for i in queue:
			print(i.data, end=" ")
		print("")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)


printLevelOrder(root)