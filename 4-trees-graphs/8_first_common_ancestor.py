# Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data
# structure. NOTE: This is not necessarily a BST
# 10, 16, 28, 36, 46, 70, 80, 96

from bst import Node
from collections import deque

# O(n) for n nodes below node1
def is_descendent(node1, node2):
    ''' Returns True if node2 is a descendent of node1 '''
    if node1 is None or node2 is None:
        return False
    if node1 == node2:
        return True
    elif is_descendent(node1.left, node2) or is_descendent(node1.right, node2):
        return True
    return False 


# O(n^2)
def first_common_ancestor(current, node1, node2, deepest=None, deepest_depth=-1, depth=0):
    ''' The deepest node such that node1 and node2 are both descendents'''
    if current is None:
        return deepest, deepest_depth

    # O(2n) = O(n)
    if is_descendent(current, node1) and is_descendent(current, node2):
        if deepest_depth is None or depth > deepest_depth:
            deepest = current
            deepest_depth = depth

    # Each O(2n) happening n times for n nodes below current
    left_node, left_depth = first_common_ancestor(current.left, node1, node2, deepest, deepest_depth, depth+1)
    right_node, right_depth = first_common_ancestor(current.right, node1, node2, deepest, deepest_depth, depth+1)

    if left_depth >= right_depth:
        return left_node, left_depth
    return right_node, right_depth
    

if __name__ == '__main__':
    tree = Node(5)
    tree.left = Node(10)
    tree.right = Node(20)
    tree.left.left = Node(0)
    tree.left.right = Node(500)
    print(tree)

    # print(is_descendent(tree, tree.right))

    print("anc")
    common, depth = first_common_ancestor(tree, tree.left.left, tree.left.right)
    print(common)
    print(depth)