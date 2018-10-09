from collections import defaultdict


class Graph:
    """The main class of our graph"""

    def __init__(self):
        # The constructor method
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        """Add edges (links) to our graph"""
        self.graph[u].append(v)
        print("{} has been connected to {}".format(u, v))

    def BFS(self, s):
        """Prints a breadth first search of the graph from vertex S."""

        for node in self.graph[s]:
            if node != s:
                print(node)


g1 = Graph()
g1.addEdge('A', 'B')
g1.addEdge('A', 'C')
g1.addEdge('A', 'D')
g1.addEdge('A', 'E')
g1.addEdge('B', 'C')
g1.addEdge('B', 'F')
g1.addEdge('A', 'A')
g1.addEdge('A', 'A')
g1.addEdge('A', 'A')
g1.addEdge('A', 'A')
g1.BFS('A')
