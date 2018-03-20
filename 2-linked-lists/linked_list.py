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
    
    def search_node(self, target_node):
        current = self.head
        while current:
            if current == target_node:
                return current
            current = current.next
        return None

    def insert(self, item):
        new_node = Node()
        new_node.item = item
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_node(self, node, prev_node=None):
        if prev_node is None:
            prev_node = self.head

        if prev_node is None:
            self.head = node
        else:
            prev_node.next = node
        
    
    def find_prev_node(self, target_item, current=None):
        if current is None:
            current = self.head

        if not current or not current.next:
            return None
        elif current.item == target_item:
            return None
        
        if current.next.item == target_item:
            return current
        else:
            return self.find_prev_node(target_item, current.next)
    
    # Inserts a new node with payload item before the target node
    def insert_before(self, item, target):
        if target is None:
            return

        new_node = Node()
        new_node.item = item
        prev_node = self.find_prev_node(target.item)

        if not prev_node:
            if self.head == target:
                new_node.next = self.head
                self.head = new_node
            else:
                return
        else: 
            new_node.next = target
            prev_node.next = new_node
        
        self.size += 1


    def delete(self, item):
        target_node = self.search(item)
        if target_node:
            prev_node = self.find_prev_node(item)
            if not prev_node:
                self.head = target_node.next
            else:
                prev_node.next = target_node.next
            self.size -= 1
    
    def delete_node(self, target_node, prev_node=None):
        if target_node is None:
            return
        
        #print(target_node)

        if prev_node is None:
            prev_node = self.find_prev_node(target_node.item)

        #print(prev_node)

        if prev_node is None: # deleting head
            self.head = self.head.next
        else:
            prev_node.next = target_node.next
    
    def find_node_less_than(self, target_item, current=None):
        if not current:
            current = self.head
        
        while current:
            if current.item < target_item:
                return current
            current = current.next
        
        return None

    def last_node(self):
        current = self.head

        while current.next:
            current = current.next
        
        return current
    

    def __str__(self):
        found = {}

        def str_helper(current):
            if not current:
                return ""
            else:
                if found.get(current, False):
                    return "(" + str(current) + ") ..."
                else:
                    found[current] = True
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
    #print(l.search(5))
    l.insert(3)
    l.insert(52)
    l.insert(5555555)
    #print(l.search(52))
    #print(l)
    #l.delete(5555555)
    #print(l.search(5555555))
    #print(l)
    l.insert(22)
    print(l)
    n = l.head.next # 52
    l.insert_before(33, n)
    print(l)
    l.insert_before(11, l.head)
    print(l)
    l.insert_before(10, l.head.next.next.next.next.next)
    print(l)
    print(l.search_node(l.head.next))
    l.delete_node(l.head.next)
    print(l)
    print(l.find_node_less_than(4))
    del l