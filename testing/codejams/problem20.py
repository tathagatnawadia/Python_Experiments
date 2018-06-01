'''
Creating a new n-ary tree
and find the most depth with increasing order of elements
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.children = None

	def add_children(self, node):
		if self.children == None:
			self.children = [node]
		else:
			self.children.append(node)

	def get_children_count(self):
		if self.children is not None:
			return len(self.children)
		return 0

	def get_children_nodes(self):
		return self.children

max_level = [1]
def DFS(node, level=1):
	print(node.data, " - ", level)
	if max_level[0] < level:
		max_level[0] = level
	if node.get_children_count() != 0:
		for i in node.get_children_nodes():
			if i.data > node.data:
				DFS(i, level+1)


a = Node(10)
b = Node(1)
c = Node(22)
d = Node(3)
a.add_children(b)
a.add_children(c)
a.add_children(d)
c.add_children(Node(22))
c.add_children(Node(88))
c.add_children(Node(11))
d.add_children(Node(44))
c.children[1].add_children(Node(199))
DFS(a, 1)
print(max_level)
