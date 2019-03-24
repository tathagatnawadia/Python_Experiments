def minDistance(candidates, source, distances):
	minimum_distance = 99999
	minimum_node = None
	for i in candidates:
		if distances[i][source] is not None and distances[i][source] < minimum_distance:
			minimum_distance = distances[i][source]
			minimum_node = i
	return minimum_node


class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.distance = [ [ None for i in range(vertices) ]
							for j in range(vertices)]
		for i in range(vertices):
			self.distance[i][i] = 0
	
	def add_connection(self, node1, node2, weight):
		self.distance[node1][node2] = weight 
		self.distance[node2][node1] = weight 

	def dijkstras(self, source):
		result = [99999 for i in range(self.vertices)]
		result[source] = 0

		queue = [i for i in range(self.vertices)]

		for i in range(self.vertices):
			next_to_visit = minDistance(queue, source, self.distance)
			queue.remove(next_to_visit)

			result[next_to_visit] = self.distance[source][next_to_visit]

			for i in range(len(self.distance[next_to_visit])):
				if self.distance[next_to_visit][i] is not None and result[i] > result[next_to_visit] + self.distance[next_to_visit][i]:
					result[i] = result[next_to_visit] + self.distance[next_to_visit][i]
			print(result)
			

a = Graph(5)
a.add_connection(0,1,3)
a.add_connection(0,2,2)
a.add_connection(0,4,4)
a.add_connection(1,2,8)
a.add_connection(2,3,1)
a.add_connection(3,4,3)

a.dijkstras(1)
