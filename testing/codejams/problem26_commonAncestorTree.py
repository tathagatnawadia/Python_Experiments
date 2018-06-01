'''
       A
      / \
     B   C
    / \   \
   D   E   F
	\     
	 G   

FIND THE Least Common Ancestor of Node G and E
FIND THE Least Common ANcestor of Node F and Node E
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

levels = {}
def findNodes(root, ancestor, value1, value2, level = 0):
	global levels
	if root:
		if level in levels.keys():
			levels[level].append((root.data, ancestor))
		else:
			levels[level] = [(root.data, ancestor)]

		findNodes(root.left, root.data, value1, value2, level+1)
		findNodes(root.right, root.data, value1, value2, level+1)

def getCommonAncestor(levels, value1, value2):
	for i in levels:
		for j in i:
			if j[1] == value1 or j[1] == value2:
				print(i, j)


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')
root.left.left.right = Node('G')


findNodes(root, None, 'G', 'E')
getCommonAncestor(levels)