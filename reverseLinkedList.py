# Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Your function reverseList is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# reverseList(head)

def reverseList(head: ListNode) -> ListNode:
  prev = None
  curr = head

  while curr:
    next = curr.next
    curr.next = prev
    prev, curr = curr, next

  return prev