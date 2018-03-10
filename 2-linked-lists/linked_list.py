class Node:
    def __init__(self):
        self.item = None
        self.next = None
    
    def __str__(self):
        return str(self.item)

class List:
    def __init__(self, items=[]):
        self.head = None
        self.size = 0
        for item in items:
            self.insert(item)
    
    # returns the Node of the item being searched for
    def search(self, target):
        def search_list_helper(current, target):
            if current == None:
                return None
            if current.item == target:
                return current
            return search_list_helper(current.next, target)

        return search_list_helper(self.head, target)

    def insert(self, item):
        new_node = Node()
        new_node.item = item
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, item):
        def find_prev_node_helper(current, target):
            if not current or not current.next:
                return None
            elif current.item == target:
                return None

            if current.next.item == target:
                return current
            else:
                return find_prev_node_helper(current.next, target)
        target_node = self.search(item)
        if target_node:
            prev_node = find_prev_node_helper(self.head, item)
            if not prev_node:
                self.head = target_node.next
            else:
                prev_node.next = target_node.next
            self.size -= 1


    def __str__(self):
        def str_helper(current):
            if not current:
                return ""
            else:
                return str(current) + " " + str_helper(current.next)
        s = str_helper(self.head)
        if not s:
            return str(None)
        else:
            return s
    
    def __len__(self):
        return self.size

if __name__ == '__main__':
    l = List()
    print(l.search(5))
    l.insert(3)
    l.insert(52)
    l.insert(5555555)
    print(l.search(52))
    print(l)
    l.delete(5555555)
    print(l.search(5555555))
    print(l)
    del l