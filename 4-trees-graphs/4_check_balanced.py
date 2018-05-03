# implement a function to check if a binary tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one
# Hints 21, 33, 49, 105, 124

from bst import Node

# O(n)
def get_height(tree, height=1, best_height=0):
    if tree is None:
        return best_height
    if height > best_height:
        best_height = height
    height_left = get_height(tree.left, height+1, best_height)
    height_right = get_height(tree.right, height+1, best_height)
    return max(height_left, height_right)

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

    # print(get_height(balanced_tree))

    print(is_balanced(balanced_tree))