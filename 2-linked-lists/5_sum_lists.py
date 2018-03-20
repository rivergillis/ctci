# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the 1's digit
# is at the head of the list. Write a function that adds the two numbers and returns
# the sum as a linked list.
#
# Ex: Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295
#    Output: (2 -> 1 -> 9). That is, 912
#
# Follow up - Suppose the digits are stored in forward order. Repeat the above
#
# Ex: Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295
#    Output: (9 -> 1 -> 2). That is, 912

from linked_list import List

# O(n)
def sum_reverse(lhs: List, rhs: List) -> List:
    lhs_current = lhs.head
    rhs_current = rhs.head

    total = []
    overflow = 0

    while lhs_current and rhs_current:
        place_total = lhs_current.item + rhs_current.item + overflow
        if place_total >= 10:
            overflow = place_total // 10
            place_total -= 10
        else:
            overflow = 0

        total.append(place_total)

        lhs_current = lhs_current.next
        rhs_current = rhs_current.next

    # Handle spots where only one side has a value
    current = None
    if lhs_current:
        current = lhs_current
    else:
        current = rhs_current
    
    while current:
        place_total = current.item + overflow
        if place_total >= 10:
            overflow = place_total // 10
            place_total -= 10
        else:
            overflow = 0
        total.append(place_total)
        current = current.next

    # Handle case where result is larger in number of places than either list
    if overflow:
        total.append(overflow)
    
    result = List()
    for item in reversed(total):
        result.insert(item)
    
    return result

# O(n + n) = O(n)
def sum_forward(lhs: List, rhs: List) -> List:
    reversed_lhs = List()
    reversed_rhs = List()

    current = lhs.head
    while current:
        reversed_lhs.insert(current.item)
        current = current.next
    
    current = rhs.head
    while current:
        reversed_rhs.insert(current.item)
        current = current.next
    
    reversed_total = sum_reverse(reversed_lhs, reversed_rhs)

    total = List()
    current = reversed_total.head
    while current:
        total.insert(current.item)
        current = current.next
    
    return total
         
if __name__ == '__main__':
    x = List([2, 9, 2]) # 617
    y = List([2, 9, 2]) # 295
    print(x)
    print(y)
    print(sum_reverse(x, y)) # 912

    x = List([7, 1, 6]) # 617
    y = List([5, 9, 2]) # 295
    print(x)
    print(y)
    print(sum_forward(x, y)) # 912