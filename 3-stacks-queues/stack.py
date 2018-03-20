class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        return self.stack.pop()
    
    def push(self, item):
        self.stack.append(item)
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self) == 0

    def __str__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)

if __name__ == '__main__':
    x = Stack()
    x.push(3)
    x.push(5)
    x.push(7)
    print(x)
    print(x.pop())
    print(x.pop())
    print(x.pop())
    print(x.is_empty())