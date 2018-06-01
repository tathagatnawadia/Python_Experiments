'''
Input : 
              1
            /   \
           2     3
         /  \   /  \
        4   5   6   7
           /     \
          8       9

Output : 11
Leaf nodes 4 and 7 are at minimum level.
Their sum = (4 + 7) = 11. 
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
leaves = []
def getSumOfMinLeaf(root, level = 0):
	global leaves
	if root is not None:
		if root.left is None and root.right is None:
			leaves.append((root.data, level))
		else:
			getSumOfMinLeaf(root.left, level+1)
			getSumOfMinLeaf(root.right, level+1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.right.left.right = Node(9)

getSumOfMinLeaf(root)
leaves = sorted(leaves, key=lambda x: x[1])
print(leaves)