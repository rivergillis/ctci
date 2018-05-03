# Implement a function to check if a binary tree is a binary tree

from bst import Node

def is_bst(tree, min_limit=None, max_limit=None):
    if tree is None:
        return True
    if min_limit is not None and tree.item < min_limit:
        return False
    if max_limit is not None and tree.item > max_limit:
        return False
    if not is_bst(tree.left, min_limit, tree.item):
        return False
    if not is_bst(tree.right, tree.item, max_limit):
        return False
    return True

if __name__ == '__main__':
    valid = Node(5)
    valid.left = Node(0)
    valid.left.left = Node(-1)
    valid.left.right = Node(1)
    valid.right = Node(10)
    valid.right.left = Node(6)
    valid.right.left.left = Node(5.5)
    valid.right.left.left.left = Node(4.9)

    print(is_bst(valid))