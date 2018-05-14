# A binary search tree was created by traversing through an array from left to
# right and inserting each element. Given a binary search tree with distinct
# elements, print all possible arrays that could have led to this tree
# Ex IN:            tree = Node(2)
#   tree.left = Node(1);    tree.right = Node(3)
#
#   Output: {2, 1, 3}, {2, 3, 1}
# Hints 39, 48, 66, 82

# Root must be first value in every array
# left subtree before right or right subtree before left

# Don't understand this. TODO: come back to this

from bst import Node
from collections import deque

def all_sequences(tree):
    result = []
    if tree is None:
        result.append(deque())
        return result
    
    prefix = deque()
    prefix.append(tree.item)

    # recurse on left and right
    left_sequence = all_sequences(tree.left)
    right_sequence = all_sequences(tree.right)

    # weave together each list from the left and right sides
    for left in left_sequence:
        for right in right_sequence:
            weaved = []
            weave(left, right, weaved, prefix)
            result.extend(weaved)
    
    return result

def weave(first, second, results, prefix):
    # if a list is empty, add remained to a cloned prefix and store result
    if not first or not second:
        result = prefix.copy()
        result.extend(first + second)
        results.append(result)
        return
    
    # recurse with head first added to prefix. removing head will damage first,
    # so we need to put it back where we found it afterwards
    head_first = first.popleft()
    prefix.append(head_first)
    weave(first, second, results, prefix)
    prefix.pop()
    first.appendleft(head_first)

    # do same with second
    head_second = second.popleft()
    prefix.append(head_second)
    weave(first, second, results, prefix)
    prefix.pop()
    second.appendleft(head_second)


if __name__ == '__main__':
    tree = Node(2)
    tree.left = Node(1)
    tree.right = Node(3)
    
    print(all_sequences(tree))