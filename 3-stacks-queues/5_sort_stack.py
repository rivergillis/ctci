# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (even a list). The stack supports the following
# operations: push, pop, peek, and is_empty

# 15, 32, 43

from stack import Stack

# This is bad, uses three stacks
def sort_bad(unsorted: Stack) -> Stack:
    result = Stack()
    tmp = Stack()

    # O(n * 2n) = O(2n^2) = O(n^2)
    while (not unsorted.is_empty()) or (not tmp.is_empty()):
        largest_found = unsorted.peek()
        # O(n)
        while not unsorted.is_empty():
            item = unsorted.pop()
            tmp.push(item)
            if item > largest_found:
                largest_found = item

        result.push(largest_found)
        has_removed_largest = False

        # O(n)
        while not tmp.is_empty():
            item = tmp.pop()
            if (item == largest_found) and (not has_removed_largest):
                has_removed_largest = True
                continue
            unsorted.push(item)
    return result

def sort(unsorted: Stack) -> Stack:
    sorted_stack = Stack()

    # O(n^2)
    while not unsorted.is_empty():
        # Get the next item
        item = unsorted.pop()
    
        number_moved = 0

        # Sort that item into the sorted stack
        # O(n)
        while not sorted_stack.is_empty():
            # Found the spot
            if sorted_stack.peek() > item:
                sorted_stack.push(item)
                break
            else:
                # Move the item onto the buffer
                number_moved += 1
                unsorted.push(sorted_stack.pop())
        
        # Need to put item into empty list as first sorted element
        if (sorted_stack.is_empty()) or (sorted_stack.peek() != item):
            sorted_stack.push(item)
        
        # Move the buffer back into the sorted stack
        # O(n)
        for i in range(number_moved):
            sorted_stack.push(unsorted.pop())
    
    return sorted_stack
        


if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(50)
    s.push(5)
    s.push(2)
    print(s)
    print(sort(s))