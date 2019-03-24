# Cut points in graph are the nodes whose removal will disconnect the graph

class Node:
	def __init__(self, value):
		self.value = value
		self.connections = []

	def add_connection(self, node):
		self.connections.append(node.value)
		node.connections.append(self.value)

	def __repr__(self):
		for con in self.connections:
			print(self.value, " is connected to ", con)
		return ""

class Graph:
	def __init__(self, *argv):
		self.connections = {}
		for arg in argv:
			self.connections[arg] = []

	def add_connection(self, src, dest):
		self.connections[src].append(dest)
		self.connections[dest].append(src)

	def bfs(self, src):
		visited = []
		to_visit = [src]
		while len(to_visit) != 0:
			next_objects = []
			while len(to_visit) != 0:
				a = to_visit.pop()
				visited.append(a)
				print(a, end = ' ')
				for node in self.connections[a]:
					if node not in visited and node not in to_visit and node not in next_objects:
						next_objects.append(node)
			to_visit = next_objects
		print()

	def findArticulationPoints(self):
		for node in self.connections.keys():
			cr1 = len(self.connections[node]) >= 2
			print(node, ' -> ',cr1)

	def findAllPaths(self, src, dest):
		to_visit = [[src]]

		while len(to_visit) != 0:
			a = to_visit.pop()
			b = a[-1]

			for nbr in self.connections[b]:
				if nbr not in a and nbr != dest:
					s = a[:]
					s.append(nbr)
					to_visit.append(s)
				if nbr == dest:
					print("Solution ", a+[dest])


	def print(self):
		for key, value in self.connections.items():
			print(key, " --> ", value)


a = Node(1)
b = Node(2)
c = Node(0)
d = Node(3)
e = Node(4)

a.add_connection(b)
a.add_connection(c)
b.add_connection(c)
c.add_connection(d)
d.add_connection(e)


G = Graph(0,1,2,3,4)
G.add_connection(1,0)
G.add_connection(1,2)
G.add_connection(2,0)
G.add_connection(0,3)
G.add_connection(3,4)
G.print()

G.findAllPaths(2, 4)



F = Graph(0, 1, 2, 3, 4, 5, 6)
F.add_connection(0,1)
F.add_connection(1,2)
F.add_connection(2,0)
F.add_connection(1,6)
F.add_connection(1,3)
F.add_connection(1,4)
F.add_connection(3,5)
F.add_connection(4,5)
F.print()
F.findAllPaths(2,5)