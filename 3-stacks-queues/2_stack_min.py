# How would you design a stack which, in addition to push and pop, has
# a function min which returns the minimum element? Push, pop and min
# should all operate in O(1) time.
# 27, 79, 

from stack import Stack

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minimum = Stack()

    def get_min(self):
        if self.minimum.is_empty():
            return None
        return self.minimum.peek()
    
    def push(self, item):
        super().push(item)
        if self.minimum.is_empty() or item < self.minimum.peek():
            self.minimum.push(item)
    
    def pop(self):
        item = super().pop()
        if item == self.minimum.peek():
            self.minimum.pop()

        return item

if __name__ == '__main__':
    x = MinStack()
    x.push(3)
    x.push(2)
    x.push(1)
    x.pop()
    x.pop()
    x.push(22)
    x.push(555)
    x.pop()
    x.push(2)
    x.pop()
    x.pop()
    print(x)
    print(x.get_min())
