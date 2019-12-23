import RemoveKthLastElementOfLinkedList
from Node import Node

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
x = RemoveKthLastElementOfLinkedList.remove_kth_from_linked_list(head, 3)
print(x)
