class Node(object):
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
    
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