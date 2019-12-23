from Node import Node

def remove_kth_from_linked_list(head, k):
    headPointer = head
    kthElement = head
    for x in range(k):
        if kthElement == None:
            return head
        kthElement = kthElement.next
    else:
        while kthElement != None:
            k -= k
            headPointer = head.next
            kthElement = kthElement.next
        if k == 0:
            headPointer.next = headPointer.next.next
    return head