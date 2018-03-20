# Imagine a literal stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previoud
# stack exceeds some threshold. Implement a data structure SetOfStacks that
# mimics this. SetOfStacks should be composed of several stacks and should create
# a new stack once the previous one exceeds capacity. SetOfStacks.push() and
# SetOfStacks.pop() should behave identically to a single stack (that is, pop()
# should return the same values as it would if there were just a single stack).
#
# Follow up: Implement a function popAt(int index) which performs a pop operation
# on a specific sub-stack.

from stack import Stack

class SetOfStacks():
    def __init__(self, capacity=3):
        self.stacks = [Stack()]
        self.current_stack = 0
        self.capacity = capacity
    
    def push(self, item):
        if len(self.stacks[self.current_stack]) >= self.capacity:
            self.stacks.append(Stack())
            self.current_stack += 1
        self.stacks[self.current_stack].push(item)
    
    def pop(self):
        item = self.stacks[self.current_stack].pop()
        if self.stacks[self.current_stack].is_empty():
            self.stacks.pop()
            self.current_stack -= 1
        return item
    
    def popAt(self, index):
        item = self.stacks[index].pop()
        if self.stacks[index].is_empty():
            del self.stacks[index]
            self.current_stack -= 1
        return item

    def __str__(self):
        result = []
        for i, stack in enumerate(self.stacks):
            result.extend([str(i), ": ", str(stack), '\n'])
        return ''.join(result[:-1])

if __name__ == '__main__':
    x = SetOfStacks()
    x.push(2)
    x.push(3)
    x.push(55)
    x.push(33)
    x.push(56)
    x.push(2000)
    x.push(3)
    for i in range(2000):
        x.push(i)
    for i in range(1900):
        x.pop()
    print(x)
    x.popAt(34)
    x.popAt(34)
    x.popAt(34)
    print(x)
    x.popAt(2)
    x.popAt(2)
    x.popAt(2)
    print(x)