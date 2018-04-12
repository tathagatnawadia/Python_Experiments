class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def MorrisTraversal(root):
	current = root
	while current is not None:

		# If no left subtree, print and make current to right subtree
		if current.left is None:
			print(current.data)
			current = current.right
		else:
			# Finding the inorder predecessor of current
			# If the left is not null
			# Getting to the rightmost of the left subtree
			pre = current.left
			while pre.right is not None and pre.right != current:
				pre = pre.right

			# Making current as right child of its inorder predecessor
			if pre.right is None:
				pre.right = current
				current = current.left

			# Revert the changes made in if part to restore 
			# original tree
			else:
				pre.right = None
				print(current.data)
				current = current.right


# Driver program to test above function
""" 
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

MorrisTraversal(root)
