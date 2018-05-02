# Given a directed graph, design an algorithm to find out whether there is a route betwen two nodes
# Hint 127

from graph import Graph
from collections import deque

# dfs
def route_between_nodes(g, node1, node2, found=set()):
    if node1 in found:
        return False
    found.add(node1)
    if node1 == node2:
        return True
    if node1 not in g.graph:
        return False
    for connected_to in g.graph[node1]:
        if route_between_nodes(g, connected_to, node2, found):
            return True
    return False

# dfs iter
def route_between_nodes_dfs_iter(g, node1, node2):
    found = set()
    to_search = [node1]
    while to_search:
        current_node = to_search.pop()
        if current_node == node2:
            return True
        for connected_to in g.graph[current_node]:
            if connected_to not in found:
                to_search.append(connected_to)
                found.add(connected_to)
    return False

def route_between_nodes_bfs(g, node1, node2):
    found = set()
    to_search = deque(node1)
    while to_search:
        current_node = to_search.popleft()
        if current_node == node2:
            return True
        for connected_to in g.graph[current_node]:
            if connected_to not in found:
                to_search.append(connected_to)
                found.add(connected_to)
    return False


if __name__ == '__main__':
    connections = [('A', 'B'), ('B', 'C'), ('A', 'D'), ('L', 'E'), ('B', 'A')]
    g = Graph(connections, directed=True)
    print(g)
    print(route_between_nodes_bfs(g, 'A', 'C'))