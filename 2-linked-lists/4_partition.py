# Write code to partition a linked list around value x, such that all
# nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only need to be
# after the elements less than x (see below). The partition element x
# can appear anywhere in the 'right partition'; it does not need
# to appear between the left and right partitions.
#
# Ex: In: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
#    Out: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from linked_list import List

# This seems sort of like a selection sort

def partition(a_list: List, partition_item: int) -> None:
    if not a_list:
        return
    
    node_before_partition_node = a_list.find_prev_node(partition_item)
    partition_node = None

    if not node_before_partition_node:
        partition_node = a_list.search(partition_item)
        if not partition_node:
            return 
    else:
        partition_node = node_before_partition_node.next

    print("Node before partition: " + str(node_before_partition_node))

    less_than_partition = a_list.find_node_less_than(partition_item, partition_node)

    print("< partition: " + str(less_than_partition))
    while less_than_partition:
        a_list.delete_node(less_than_partition)
        print(a_list)
        a_list.insert_before(less_than_partition.item, partition_node)
        less_than_partition = a_list.find_node_less_than(partition_item, partition_node)
        print("< partition: " + str(less_than_partition))

if __name__ == '__main__':
    x = List([5, 2, 3, 6, 9, 0, 1])
    print(x)
    partition(x, 6)
    print(x)
