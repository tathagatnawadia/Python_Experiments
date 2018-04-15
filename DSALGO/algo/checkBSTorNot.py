class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def isBST(root, left=None, right=None):
	# Base condition
	if root is None:
		return True

	# If node is on the left the it should be smaller than its ancestor
	if left is not None and root.data < left.data:
		return False
	# If node is on right should be greater than ancestor
	if right is not None and root.data > right.data:
		return False
	
	return isBST(root.left, left, root) and isBST(root.right, root, right)


# Driver program to test above function
""" 
Constructed binary tree is
            15
          /   \
        11      33
      /  \
      1    14
"""
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(isBST(root))