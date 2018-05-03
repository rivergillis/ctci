# You are given a list of projects and a list of dependencies (which is
# a list of pairs of projects, where the second project is dependent on the
# first project). ALl of a project's dependencies must be built before the
# project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.
#
# Ex: In:
#   projects: a, b, c, d, e, f
#   dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
#
# Hints 26, 47, 60, 85, 125, 133

from graph import Graph
from collections import deque
from collections import defaultdict

# We build a dependency graph
# a directed graph where the dependencies point toward the dependents
# start at an independent dependency and bfs through the graph
# then build anything not connected

def can_build(project, has_built, total_deps):
    need_to_be_built = total_deps[project]
    for need in need_to_be_built:
        if need not in has_built:
            return False
    return True


# Probably better solved with two graphs instead of total_deps
# Total deps is acting as a reverse dependency graph
def build_order(projects, dependencies):
    is_dependent = set()
    dependecy_graph = Graph(directed=True)
    total_deps = defaultdict(set)

    for proj, dependent in dependencies:
        dependecy_graph.add(proj, dependent)
        is_dependent.add(dependent)
        total_deps[dependent].add(proj)
    
    # We have a start building somewhere, these will work
    independent = set(projects) - is_dependent

    order = []
    built = set()
    
    # BFS
    found = set()
    to_search = deque(independent)
    while to_search:
        current_node = to_search.popleft()
        for connected_to in dependecy_graph.graph[current_node]:
            if connected_to not in found:
                to_search.append(connected_to)
                found.add(connected_to)
        if can_build(current_node, built, total_deps):
            order.append(current_node)
            built.add(current_node)
        else:
            to_search.append(current_node)
            # check if we need to kill it here?
    
    return order


if __name__ == '__main__':
    projects = ['a', 'b']
    dependencies = [('b', 'a')]
    order = build_order(projects, dependencies)
    print(order)

    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    order = build_order(projects, dependencies)
    print(order)
