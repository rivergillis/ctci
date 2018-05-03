# Write an algorithm to find the "next" node (i.e., in order successor)
# of a given node in a binary search tree. You may assume that each 
# node has a link to its parent

from bst_parent import Node

# successor is leftmost leaf of right subtree (sometimes)

# O(logn)
def successor(tree):
    if tree is None:
        return None
    # if we have a right child, successor is leftmost leaf of right subtree
    if tree.right:
        current = tree.right
        while current and current.left:
            current = current.left
        return current
    # if we have no right child, move up until we find the first node larger than tree
    current = tree
    while current:
        if current.item > tree.item:
            return current
        current = current.parent
    # no successor
    return None

if __name__ == '__main__':
    tree = Node(5)
    tree.left = Node(2, parent=tree)
    tree.right = Node(10, parent=tree)
    tree.right.right = Node(20, parent=tree.right)
    tree.right.left = Node(8, parent=tree.right)
    print(successor(tree.right.left))
