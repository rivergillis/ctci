# Implement a MyQueue class which implements a queue using two stacks.

from stack import Stack

class MyQueue:
    def __init__(self):
        self.data = Stack()
        self.reserve = Stack()
    
    # Add an item to the end of the queue
    # O(1)
    def add(self, item):
        while not self.reserve.is_empty():
            self.data.push(self.reserve.pop())
        self.data.push(item)
    
    # Remove the first item in the list
    # O(2n) = O(n)
    def remove(self):
        while len(self.data) > 1:
            self.reserve.push(self.data.pop())
        item = self.data.pop()

        while not self.reserve.is_empty():
            self.data.push(self.reserve.pop())
        return item

    # Return the top of the queue
    # O(n)
    def peek(self):
        while len(self.data) > 1:
            self.reserve.push(self.data.pop())
        return self.data.peek()
    
    # Return true iff the queue is empty
    def is_empty(self):
        return self.data.is_empty()
    
    def __str__(self):
        return str(self.data) + " res: " + str(self.reserve)

if __name__ == '__main__':
    q = MyQueue()
    q.add(3)
    q.add(4)
    q.add(5)
    print(q)
    print(q.remove())
    print(q.is_empty())
    print(q)
    print(q.peek())
    print(q)
    print(q.peek())
    print(q)
    q.add(36)
    print(q)