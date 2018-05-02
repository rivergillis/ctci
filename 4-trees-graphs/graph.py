from collections import defaultdict

class Graph(object):
    def __init__(self, connections, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_connections(connections)
    
    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)
    
    def add(self, node1, node2):
        self.graph[node1].add(node2)
        if not self.directed:
            self.graph[node2].add(node1)
    
    def remove(self, node):
        for x, connected_to in self.graph.items():
            try:
                connected_to.remove(node)
            except KeyError:
                pass
        try:
            del self.graph[node]
        except KeyError:
            pass
    def __str__(self):
        return f"{self.__class__.__name__} ({dict(self.graph)})"

if __name__ == '__main__':
    connections = [('A', 'B',), ('B', 'C'), ('A', 'D')]
    g = Graph(connections, directed=True)
    print(g)
    g.remove('C')
    print(g)
    g.remove('B')
    print(g)