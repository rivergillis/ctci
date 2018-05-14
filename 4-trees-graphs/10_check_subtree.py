# T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create
# an algorithm to determine if T2 is a subtree of T1
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree
# of n is identical to T2. That is, if you cut off the tree at node n, the two
# trees would be identical
#
# Hints 4, 11, 18, 31, 37

from bst import Node

# Assume no duplicates
# Find t2 root in t1, then follow through the branches to verify they are equal

def find(tree, target_node):
    target_val = target_node.item
    while tree:
        if tree.item == target_val:
            return tree
        elif tree.item < target_val:
            tree = tree.right
        else:
            tree = tree.left
    return None

def verify(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif (t1 is None and t2 != None) or (t1 != None and t2 is None):
        return False
    elif t1.item != t2.item:
        return False
    elif not verify(t1.left, t2.left):
        return False
    elif not verify(t1.right, t2.right):
        return False
    
    return True

def check_subtree(t1, t2):
    """ Returns true if t2 is a subtree of t1 """
    t1_node = find(t1, t2)
    if t1_node is None:
        return False
    return verify(t1_node, t2)

if __name__ == '__main__':
    t1 = Node(5)
    t1.left = Node(0)
    t1.right = Node(10)
    t1.right.right = Node(50)
    t1.right.right.right = Node(500)

    t2 = Node(10)
    t2.right = Node(50)
    t2.right.right = Node(500)

    print(check_subtree(t1, t2))
