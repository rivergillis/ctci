# Given a sorted (increasing order) array with unique integer elements
# write an algorithm to create a BST with minimal height
# hints 19, 73, 116

class Node(object):
    def __init__(self, item, left=None, right=None):
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

def minimal_tree(a_list):
    pass

if __name__ == '__main__':
    a = [0, 1, 5, 9, 10]
    n = minimal_tree(a)
    print(n)