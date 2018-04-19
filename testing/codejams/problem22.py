'''
2 nodes are swapped in the BST, find them out and swap them back to restore balance in the universe
'''


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

INT_MAX = 999999999
INT_MIN = -INT_MAX
voilations = []
def isBST(head, min, max):
	global voilations
	if head is None:
		return True
	if head:
		if head.data < min or head.data > max:
			voilations.append(head)
			return False
		leftSubtreeResult = isBST(head.left, min, head.data-1)
		rightSubtreeResult = isBST(head.right, head.data+1, max)
		return (leftSubtreeResult and rightSubtreeResult)


'''
		10
	    / \
	    5  3
	    /\
		2 20
'''	
root = Node(10)
root.right = Node(3)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(20)

isBST(root, INT_MIN, INT_MAX)

# Swap the 2 voilated nodes
temp = voilations[0].data
voilations[0].data = voilations[1].data
voilations[1].data = temp
