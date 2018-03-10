# Write code to remove duplicates form an unsorted linked list.
# How would you solve this if a temporary buffer was not allowed?

from linked_list import List

# O(n)
def remove_dups(a_linked: List) -> None:
    seen = {}
    current = a_linked.head

    # O(n)
    while current:
        seen[current.item] = seen.get(current.item, 0) + 1
        current = current.next
    
    # O(n)
    for value, count in seen.items():
        while count > 1:
            a_linked.delete(value)
            count -= 1

# O(n^2)
def remove_dups_no_buffer(a_linked: List) -> None:
    current = a_linked.head

    # O(n)
    while current.next:
        searcher = a_linked.head
        while searcher: # O(2n = n)
            if searcher.item == current.item and searcher != current:
                a_linked.delete(searcher.item) # O(n)
                break
            searcher = searcher.next
        current = current.next

if __name__ == '__main__':
    x = List([4, 2, 4, 4, 3, 1, 1, 1, 1, 2, 3, 4, 0, -1])
    print(x)
    remove_dups(x)
    print(x)

    y = List([4, 2, 4, 4, 3, 1, 1, 1, 1, 2, 3, 4, 0, -1])
    print(y)
    remove_dups_no_buffer(y)
    print(y)