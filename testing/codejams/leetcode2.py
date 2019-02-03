'''
https://leetcode.com/articles/all-nodes-distance-k-in-binary-tree/
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

rootAnsectors = []
solution = []
global keyNode
keyNode = None


def getAncestors(root, key, dist, level=0):
	if root.data == key:
		keyNode = (root, level)
		return True

	if root.left is not None:
		if getAncestors(root.left, key, dist, level+1):
			if level + 1 == dist:
				solution.append(root.data)
			rootAnsectors.append((root, "left", level, root.data))
			return True

	if root.right is not None:
		if getAncestors(root.right, key, dist, level+1):
			if level + 1 == dist:
				solution.append(root.data)
			rootAnsectors.append((root, "right", level, root.data))
			return True

	return False


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

getAncestors(root, 2, 2)
print(rootAnsectors)
print(solution)
print(keyNode)