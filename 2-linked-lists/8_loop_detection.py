# Given a circular linked list, implement an algo that returns the node at the
# beginning of the loop.
#
# Defn: A circular linked list is a LL in which a node's next pointer points
# to an earlier node, so as to make a loop in the linked list.
#
# Ex: In: A -> B -> C -> D -> E -> C (Same C as earlier)
# Output: C

from linked_list import List, Node

# O(n)
def find_loop(a_list: List) -> Node:
    found = {}

    current = a_list.head
    while current:
        if found.get(current, False):
            return current
        else:
            found[current] = True
        current = current.next
    
    return None

if __name__ == '__main__':
    x = List(['A', 'B', 'C', 'D', 'E'])
    n = x.head.next.next
    x.insert_node(n, prev_node=x.last_node())
    print(n)
    print(x)

    y = List('f')

    print(find_loop(x))
    print(find_loop(y))