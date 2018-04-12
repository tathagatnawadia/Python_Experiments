class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

'''

			 10
		    / \
		    4  9
		    /\ 
		    1 2
		    \4
'''
head = Node(10)

head.left = Node(4)
head.right = Node(9)

head.left.left = Node(1)
head.left.right = Node(2)

head.left.left.right = Node(4)

def getLeafNodesSum(head, leaf_nodes_sum):
	if head is None:
		return
	if head.left == None and head.right == None:
		leaf_nodes_sum += head.data
		return
	getLeafNodesSum(head.right, leaf_nodes_sum)
	getLeafNodesSum(head.left, leaf_nodes_sum)

leaf_nodes_sum = 0
getLeafNodesSum(head, leaf_nodes_sum)
print(leaf_nodes_sum)