# Implment an algorithm to find the kth to last element of a singly linked list.

from linked_list import List

# O(n-k)
def kth_to_last(a_list: List, k: int) -> List:
    moves = len(a_list) - k
    current = a_list.head

    while moves > 0:
        current = current.next
        moves -= 1
    
    return current

if __name__ == '__main__':
    x = List([1, 2, 3, 4])
    print(x)
    print(kth_to_last(x, 2)) # 2