from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self._vertices = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if u not in self._vertices:
            self._vertices.append(u)
        if v not in self._vertices:
            self._vertices.append(v)

    def __str__(self):
        return str(self.graph)

    def getVertices(self):
        return self._vertices


class GraphTraversals():
    def __init__(self):
        self._bfs = []
        self._dfs = []

    def markVisited(self, visitedList, visitedNode):
        visitedList[visitedNode] = True
        return visitedList

    def initVisited(self, g):
        return [False] * (len(g.graph))

    def saveVisitSequence(self, sequenceList, node):
        sequenceList.append(node)

    def BFS(self, g, s):
        visited = self.initVisited(g)
        # Creating a queue and pushing the first vertex "s"
        queue = []
        queue.append(s)

        while queue:
            # Popping from the queue and marking it visisted, saving it in the saveVisitSequence
            s = queue.pop(0)
            visited = self.markVisited(visited, s)
            self.saveVisitSequence(self._bfs, s)
            # Iterating from all siblings from the popped vertex
            for i in g.graph[s]:
                if visited[i] == False:
                    # Queing all the siblings from vertex "s"
                    queue.append(i)
                    #visited = self.markVisited(visited, i)
        return self._bfs

    def DFSUtil(self, g, v, visited):
        visited[v] = self.markVisited(visited, v)
        self.saveVisitSequence(self._dfs, v)
        for i in g.graph[v]:
            if visited[i] == False:
                self.DFSUtil(g, i, visited)

    def DFS(self, g, v):
        visited = self.initVisited(g)
        self.DFSUtil(g, v, visited)
        return self._dfs

    def topologicalSort(self, g):
        visited = self.initVisited(g)
        stack = []

        for i in range(len(g.getVertices())):
            print(i)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g)

c = GraphTraversals()
# This gives a list of sequence for BFS traversal
print(c.BFS(g,2))
# This gives a list of sequecne for DFS traversal
print(c.DFS(g,2))

c.TopologicalSort(g)
# TODO : generalising graph implementation for any object
