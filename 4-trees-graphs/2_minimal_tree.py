# Given a sorted (increasing order) array with unique integer elements
# write an algorithm to create a BST with minimal height
# hints 19, 73, 116

class Node(object):
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
    
    def __str__(self):
        total = []
        if self.left:
            total.append(str(self.left))
            total.append(', ')
        total.append(str(self.item))
        if self.right:
            total.append(', ')
            total.append(str(self.right))
        return ''.join(total)
    
    def __repr__(self):
        return str(self)

# This is sort of like a binary search in reverse
def minimal_tree(a_list):
    if not a_list:
        return None
    tree = Node()
    midpoint = len(a_list) // 2
    tree.item = Node(a_list[midpoint])
    if len(a_list) > 1:
        tree.left = minimal_tree(a_list[0:midpoint])
        tree.right = minimal_tree(a_list[midpoint+1:len(a_list)])
    return tree


if __name__ == '__main__':
    a = [0, 1, 5, 9, 10]
    n = minimal_tree(a)
    print(n)