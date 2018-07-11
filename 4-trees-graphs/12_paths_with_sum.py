# You are given a binary tree in which each node contains an integer value
# which might be postive or negative. Design an algorithm to count the number
# of paths that sum to a given value. The path does not need to start or end
# at the root or a leaf, but it must go downwards (traveling only from parent
# nodes to child nodes).
# Hints 6, 14, 52, 68, 77, 87, 94, 103, 108, 115

from bst import Node
from collections import defaultdict

# O(nlogn)
def count_paths_with_sum(root, target_sum):
    if root is None:
        return 0
    # Count paths with sum starting from root
    paths_from_root = count_paths_with_sum_from_node(root, target_sum, 0)

    # try the left and right nodes
    paths_on_left = count_paths_with_sum(root.left, target_sum)
    paths_on_right = count_paths_with_sum(root.right, target_sum)

    return paths_from_root + paths_on_left + paths_on_right

def count_paths_with_sum_from_node(node, target_sum, current_sum):
    if node is None:
        return 0

    current_sum += node.item
    
    total_paths = 0
    if current_sum == target_sum: # Found a path from the root
        total_paths += 1
    
    total_paths += count_paths_with_sum_from_node(node.left, target_sum, current_sum)
    total_paths += count_paths_with_sum_from_node(node.right, target_sum, current_sum)
    return total_paths


def paths_with_sum(value):
    pass

if __name__ == '__main__':
    t = Node(5)
    t.left = Node(1)
    t.right = Node(4)
    t.right.right = Node(1)
    t.right = Node(0)
    print(count_paths_with_sum(t, 6))