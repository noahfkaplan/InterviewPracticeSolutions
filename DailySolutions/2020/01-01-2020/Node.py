class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    newHead = current = Node(None)
    headA = lists[0]
    headB = lists[1]
    while headA != None or headB != None:
        if headA == None:
            current.next = headB
            return newHead
        elif headB == None:
            current.next = headA
            return newHead
        elif headA.val > headB.val:
            current.next = Node(headB.val)
            current = current.next
            headB = headB.next
        else:
            current.next = Node(headA.val)
            current = current.next
            headA = headA.next
            
    return newHead