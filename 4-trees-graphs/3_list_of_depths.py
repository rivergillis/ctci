# Given a binary tree, design an algorithm which creates a linked list of all
# the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists)
# Hints 107, 123, 135

from bst import Node
from collections import defaultdict

class LinkedList(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None
    
    def __str__(self):
        total = []
        current = self
        while current:
            total.append(str(current.item))
            current = current.next
        return ' -> '.join(total)
    
    def __repr__(self):
        return str(self.item)
    
    def add(self, item):
        if self.item is None:
            self.item = item
            return
        new_next = LinkedList(self.item)
        new_next.next = self.next
        self.next = new_next
        self.item = item


# def find_depth(tree, target_item):
#     depth = 0
#     current = tree
#     while current:
#         if current.item == target_item:
#             return depth
#         if target_item < current.item:
#             current = current.left
#         else:
#             current = current.right
#         depth += 1
#     return None


# strategy, traverse the bst and keep a record of the depth of everything
# Keep a dict of depth mappings to linked lists
def list_of_depths(tree, depths, depth=0):
    if tree is None:
        return
    depths[depth].add(tree.item)
    list_of_depths(tree.left, depths, depth+1)
    list_of_depths(tree.right, depths, depth+1)

if __name__ == '__main__':
    tree = Node(0)
    tree.left = Node(-2)
    tree.left.left = Node(-3)
    tree.left.right = Node(-1)
    tree.right = Node(5)
    tree.right.right = Node(6)
    
    depths = defaultdict(LinkedList)
    list_of_depths(tree, depths)
    print(dict(depths))