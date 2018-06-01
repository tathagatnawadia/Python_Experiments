'''
Given a rooted tree, and two nodes which is in the tree, find the Lowest common ancestor of both the nodes.
The LCA for two nodes u and v is defined as the farthest node from root that is ancestor to both u and v.
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

class ReverseNode:
	def __init__(self, data):
		self.data = data
		self.parent = None

def printNodeList(node_list):
	for i in node_list:
		print(i.data)
	print("*****")

def searchLevelOrder(root, order={}, index=0):
	if index == 0:
		order[index] = [root]
	order[index+1] = []
	end_recur = True
	for i in order[index]:
		if i.left is not None:
			end_recur = False
			order[index+1].append(i.left)
		if i.right is not None:
			end_recur = False
			order[index+1].append(i.right)
	# No more nodes to visit
	if end_recur == True:
		return
	else:
		searchLevelOrder(root, order, index+1)

def constructReverseTree(root, order={}, reverse_tree=[],index=0):
	if index == 0:
		order[index] = [root]
	order[index+1] = []
	end_recur = True
	for i in order[index]:
		if i.left is not None:
			end_recur = False
			i.left.parent = i
			order[index+1].append(i.left)
		if i.right is not None:
			end_recur = False
			i.right.parent = i
			order[index+1].append(i.right)
		#Checking for leaf nodes only and adding them to reverse tree
		if i.left is None and i.right is None:
			reverse_tree.append(i)
	if end_recur == True:
		return
	else:
		constructReverseTree(root, order, reverse_tree, index+1)


# Constructing a tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

o = {}
searchLevelOrder(root, o, 0)
for i in o:
	printNodeList(o[i])

p = {}
l = []
constructReverseTree(root, p, l, 0)
for i in p:
	printNodeList(p[i])
for i in l:
	print(i.data, "->", i.parent.data)
#a,b = input().split()
