# implement a function to check if a binary tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one
# Hints 21, 33, 49, 105, 124

from bst import Node
from collections import defaultdict

# O(n)
def get_height(tree, height=1, best_height=0):
    if tree is None:
        return best_height
    if height > best_height:
        best_height = height
    height_left = get_height(tree.left, height+1, best_height)
    height_right = get_height(tree.right, height+1, best_height)
    return max(height_left, height_right)

def get_heights(tree, heights, height=1, path=[]):
    if tree is None:
        return path
    path.append(tree)
    path_left = get_heights(tree.left, heights, height+1, path)
    for i, node in enumerate(path_left):
        current_height = heights.get(node, 0)
        measured_height = height - i
        if measured_height > current_height:
            heights[node] = measured_height
    path_right = get_heights(tree.right, heights, height+1, path)
    for i, node in enumerate(path_right):
        current_height = heights.get(node, 0)
        measured_height = height - i
        if measured_height > current_height:
            heights[node] = measured_height
    return path

# O(n)
def get_paths(tree):
    # We've reached a null node, nothing to add to the list
    if tree is None:
        return []
    # We've reached a leaf, return the current item as a list
    if tree.left is None and tree.right is None:
        return [tree]
    # Add up the left and right paths
    return [[tree] + [l] for l in 
        get_paths(tree.left) + get_paths(tree.right)]

def set_heights(paths):
    heights = defaultdict(lambda: 0)
    for path in paths:
        height = len(path)
        for current, node in enumerate(path):
            measured_height = height - current
            if heights[node] < measured_height:
                heights[node] = measured_height
    return dict(heights)

# O(n^2)
def is_balanced(tree):
    if tree is None:
        return True
    height_left = get_height(tree.left)
    height_right = get_height(tree.right)
    if abs(height_left - height_right) > 1:
        return False
    if not is_balanced(tree.left):
        return False
    if not is_balanced(tree.right):
        return False
    return True

if __name__ == '__main__':
    balanced_tree = Node(2)
    balanced_tree.left = Node(1)
    balanced_tree.left.left = Node(0)
    balanced_tree.left.left.left = Node(-1)
    balanced_tree.left.left.right = Node(0.5)
    balanced_tree.left.right = Node(1.5)
    balanced_tree.right = Node(8)
    balanced_tree.right.left = Node(7)
    balanced_tree.right.left.left = Node(6)
    balanced_tree.right.right = Node(20)

    test = Node(5)
    test.left = Node(2)
    test.right = Node(10)

    # heights = {}
    # get_heights(test, heights)
    # print(heights)
    # heights = get_paths(balanced_tree)
    # print(heights)
    # print(set_heights(heights))

    # print(get_height(balanced_tree))

    print(is_balanced(balanced_tree))