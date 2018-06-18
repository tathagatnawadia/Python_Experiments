class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.down = None


'''
Creating this stupid linkedlist
5 -> 10 -> 19 -> 28
|    |     |     |
V    V     V     V
7    20    22    35
|          |     |
V          V     V
8          50    40
|                |
V                V
30               45
'''
root = Node(5)
root.down = Node(7)
root.down.down = Node(8)
root.down.down.down = Node(30)

root.right = Node(10)
root.right.down = Node(20)

root.right.right = Node(19)
root.right.right.down = Node(22)
root.right.right.down.down = Node(50)

root.right.right.right = Node(28)
root.right.right.right.down = Node(35)
root.right.right.right.down.down = Node(40)
root.right.right.right.down.down.down = Node(45)

def printAllRight(node):
	while node is not None:
		print(node.data," -> ", end="")
		node = node.right
	print()


def put(node, lookup):
	print(node.data, " - ", lookup.data)
	prev = lookup
	while lookup.data < node.data:
		prev = lookup
		lookup = lookup.right
		if lookup is None:
			break
	prev.right = node
	node.right = lookup
	return node


def flatten(root):
	iteration = 0
	root_b = root
	while root.right is not None:
		lookup = root
		while root.down is not None:
			tempNode = root.down 
			lookup = put(tempNode, lookup)
			root.down = root.down.down
			tempNode.down = None
		printAllRight(root_b)
		root = root.right
		print("Next node : ", root.data)


flatten(root)
