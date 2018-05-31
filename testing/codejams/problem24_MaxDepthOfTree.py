'''
Input : 
              1
            /   \
           2     3
         /  \   /  \
        4   5   6   7
           /     \
          8       9

Max depth of the tree
Output : 3
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def maxDepth(node):
	if node is None:
		return 0
	ldepth = maxDepth(node.left)
	rdepth = maxDepth(node.right)

	if ldepth > rdepth:
		return ldepth + 1
	else:
		return rdepth + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.right.left.right = Node(9)

max_depth_of_root = maxDepth(root)
print(max_depth_of_root)