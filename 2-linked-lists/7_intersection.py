# Given two singly linked lists, determine if the two lists intersect.
# Return the intersecting node. Note that the intersection is defined based
# on reference, not value. That is, if the kth node of the first linked list
# is the exact same node (by reference) as the jth node of the second linked
# list, then they are intersecting

from linked_list import List, Node

# O(n^2)
def intersection(lhs: List, rhs: List) -> Node:
    lhs_current = lhs.head
    while lhs_current:
        rhs_current = rhs.head
        while rhs_current:
            if lhs_current == rhs_current:
                return lhs_current
            rhs_current = rhs_current.next
        lhs_current = lhs_current.next
    

if __name__ == '__main__':
    x = List([1, 2, 3, 4])
    n = Node()
    n.item = 17
    n.next = x.head.next
    x.insert_node(n)
    y = List([5, 6, 7])
    y.insert_node(n, y.head.next.next)

    print(x)
    print(y)
    print(intersection(x, y))