# Random Node: You are implementing a binary tree class from scratch which,
# in addition to insert, find, and delete, has a method getRandomNode() which
# returns a random node from the tree. All nodes should be equally likely
# to be chosen. Design and implement an algorithm for getRandomNode, and
# explain how you would implement the rest of the methods
# Hints 42, 54, 62, 75, 89, 99, 112, 119

# idea: generate a random path
# or generate a random L/R/Stop at each intersection

import random

class Node:
    def __init__(self, item=None):
        self.item = item
        self.size = 1
        self.left = None
        self.right = None
    
    def __str__(self):
        total = []
        if self.left:
            total.append(str(self.left))
            total.append(' <- ')
        total.append(str(self.item))
        if self.right:
            total.append(' -> ')
            total.append(str(self.right))
        return ''.join(total)
    
    def __repr__(self):
        return str(self.item)
    
    def __len__(self):
        return self.size

class Tree:
    def __init__(self):
        self.root = None
    
    def __str__(self):
        return str(self.root)
    
    def __len__(self):
        return self.root.size
    
    def insert(self, item):
        """ Inserts a new node with item item into T """
        # Find the node that would exist
        prev = None
        current = self.root
        if not current:
            self.root = Node(item)
            return
        while current:
            prev = current
            current.size += 1
            if current.item <= item:
                current = current.right
            else:
                current = current.left
        if prev.item <= item:
            prev.right = Node(item)
        else:
            prev.left = Node(item)

    def find(self, item):
        """ Returns the node in T which corresponds to item, or None """
        current = self.root
        while current:
            if current.item == item:
                return current
            if current.item < item:
                current = current.right
            else:
                current = current.left
        return None
    
    def find_prev(self, node):
        """ Returns the node that is the rightmost child of the left subtree of node
        , also returns the parent node for that child as a (child, parent) tuple """
        prev = None
        current = node
        if not current:
            return None, None

        # Move left
        prev = current
        current = current.left
        if not current:
            return None, None
        
        # Get rightmost child
        while current.right:
            prev = current
            current = current.right
        
        return current, prev
        

    def delete(self, item):
        """ Removes the node corresponding to item if it exists in T """
        # If no children, just remove it from the parent
        # If one child, remove and give the child its place
        # If two, replace twith rightmost child of left subtree
        prev = None
        current = self.root

        to_decrease = []

        while current:
            to_decrease.append(current)
            if current.item == item:
                break
            elif current.item < item:
                prev = current
                current = current.right
            else:
                prev = current
                current = current.left
        if not current:
            return

        for n in to_decrease:
            n.size -= 1
        
        # No children
        if current.left is None and current.right is None:
            if prev.left == current:
                prev.left = None
            else:
                prev.right = None
            return
        
        # One child
        if current.left is None or current.right is None:
            child = None
            if current.left:
                child = current.left
            else:
                child = current.right
            current.left = None
            current.right = None
            current.item = child.item
            return
        
        # Two children
        replacement, replacement_parent = self.find_prev(current)
        if not replacement or not replacement_parent:
            return
        current.item = replacement.item
        replacement_parent.size -= 1
        if replacement_parent.left == replacement:
            replacement_parent.left = None
        else:
            replacement_parent.right = None
    
    def get_random_node(self):
        """ Ensures each node has the same 1/N chance of being picked """
        current = self.root
        while current:
            left_size = 0 if current.left is None else current.left.size
            option = random.randint(0, current.size-1)
            if option < left_size:
                current = current.left
            elif option == left_size:
                return current
            else:
                current = current.right

if __name__ == '__main__':
    t = Tree()
    t.insert(20)
    t.insert(10)
    t.insert(30)
    t.insert(15)
    t.insert(0)
    print(t)
    print(t.root.size)
    counts = {}
    for i in range(2000):
        ran = t.get_random_node()
        counts[ran] = counts.get(ran, 0) + 1
    print(counts)
