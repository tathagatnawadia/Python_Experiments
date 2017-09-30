V,E = list(map(int, input().split()))
Vertices = list(range(1,V+1))
removed_nodes = []
man = {}
woman = {}

def insert_graph(graph, v1, v2, road_type=None):
	if v1 not in graph.keys():
		graph[v1] = []
	if road_type == None:
		graph[v1].append(v2)
	else:
		graph[v1].append((v2,road_type))
	return graph

def get_edges(graph, road_type):
	qualifiying_edges = []
	for vertex, edges in graph.items():
		for edge in edges:
			if edge[1] == road_type:
				qualifiying_edges.append((vertex, edge[0]))
	return qualifiying_edges

def remove_edge(graph, v1, v2):
	if v1 in graph.keys() and v2 in graph[v1]:
		graph[v1].remove(v2)
	if v2 in graph.keys() and v1 in graph[v2]:
		graph[v2].remove(v1)
	return graph

def remove_road(graph, v1, v2, type):
	if v1 in graph.keys() and (v2,type) in graph[v1]:
		graph[v1].remove((v2, type))
	if v2 in graph.keys() and (v1, type) in graph[v2]:
		graph[v1].remove((v1, type))
	removed_nodes.append((v1, v2, type))
	return graph

def preprocess(graph):
	new_graph = {}
	for key, value in graph.items():
		for v in value:
			new_graph = insert_graph(new_graph,key, v[0])
			new_graph = insert_graph(new_graph,v[0], key)
	return new_graph

def DFSUtil(g, v, visited):
    visited.append(v)
    if v in g.keys():
	    for i in g[v]:
	        if i not in visited:
	            DFSUtil(g, i, visited)

def DFS(graph, v):
	visited = []
	DFSUtil(graph, v, visited)
	return visited

def is_connected(g):
	result = DFS(g, 1)
	result.sort()
	if result == Vertices:
		return True
	else:
		return False

edge_counter = 1
while edge_counter <= E:
	edge_counter = edge_counter + 1
	v1, v2, road_type =  list(map(int, input().split()))
	if road_type == 3:
		man = insert_graph(man, v1, v2, road_type)
		woman = insert_graph(woman, v1, v2, road_type)
	elif road_type == 1:
		man = insert_graph(man, v1, v2, road_type)
	else:
		woman = insert_graph(woman, v1, v2, road_type)


# Removing men only edges and check for impact
for edge in get_edges(man, 1):
	g = remove_edge(preprocess(man), edge[0], edge[1])
	if is_connected(g):
		man = remove_road(man, edge[0], edge[1], 1)

# Removing woman only edges and check for impact
for edge in get_edges(woman, 2):
	g = remove_edge(preprocess(woman), edge[0], edge[1])
	if is_connected(g):
		woman = remove_road(woman, edge[0], edge[1], 2)

# Removing men and woman edges and check for impact
for edge in get_edges(man, 3):
	g1 = remove_edge(preprocess(man), edge[0], edge[1])
	g2 = remove_edge(preprocess(woman), edge[0], edge[1])
	if is_connected(g1) and is_connected(g2):
		man = remove_road(man, edge[0], edge[1], 3)
		woman = remove_road(woman, edge[0], edge[1], 3)

print(len(removed_nodes))

# 5 7
# 1 2 3
# 2 3 3
# 3 4 3
# 5 3 2
# 5 4 1
# 5 2 2
# 1 5 1
