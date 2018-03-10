# Implment an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly
# linked list, given only access to that node.
# Input: node c from linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

from linked_list import List, Node

# O(n)
def delete_node(a_list: List, target: Node) -> None:
    if len(a_list) <= 2:
        return

    prev_node = a_list.head
    current_node = prev_node.next

    # O (n)
    while current_node.next:
        if current_node == target:
            prev_node.next = target.next
            a_list.size -= 1
            return
        prev_node = current_node
        current_node = current_node.next

if __name__ == '__main__':
    x = List([1, 2, 3, 4])
    print(x)
    n = x.head.next
    delete_node(x, n)
    print(x)