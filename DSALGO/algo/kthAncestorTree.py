'''
Find the kth Ancestor of a node in a tree
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def kthAncestor(node, key, level=0, solution=[]):
	if node is None:
		return None
	if node.data == key:
		return node

	result1 = kthAncestor(node.left, key, level+1, solution)
	result2 = kthAncestor(node.right, key, level+1, solution)

	if result1 is not None or result2 is not None:
		solution.append((node.data, level))
		if result1 is not None:
			return result1
		else:
			return result2

# Driver program to test above function
""" 
Constructed binary tree is
            1
          /   \
        2      3
      /  \     \ 
    4     5.    77
    \.   / \
     6  19  33

"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(77)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(6)
root.left.right.left = Node(19)
root.left.right.right = Node(33)


solution = []
kthAncestor(root, 19, 0, solution)

#Printing all levels
for data, level in solution:
	print(level, "th level -> ", data)
