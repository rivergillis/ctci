# Implement a function to check if a linked list is a palindrome

from linked_list import List

# O(n)
def is_palindrome(a_list: List) -> List:
    letters = {}

    # O (n)
    current = a_list.head
    while current:
        letters[current.item] = letters.get(current.item, 0) + 1
        current = current.next
    
    # print(letters)

    has_odd = False

    for letter, count in letters.items():
        if count % 2 != 0:
            if has_odd:
                return False
            else:
                has_odd = True

    return True


if __name__ == '__main__':
    x = List(['e'])
    print(x)
    print(is_palindrome(x))

    y = List(['a', 'b', 'b', 'a'])
    print(y)
    print(is_palindrome(y))

    z = List(['b', 'a', 'c', 'a', 'b'])
    print(z)
    print(is_palindrome(z))
