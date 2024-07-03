# Checking for cycle in linked list

# Matching 
# 2-pointer method - faster skips one node, slower pointer goes node by node 
# if the fast pointer reaches a null node, then there is no cycle

# Plan /Pseudocode 
# 1 -> 2 -> 3 -> (loop back to 1) 

"""
Explaining it out...
1. Initialize the pointers: 1 fast goes 2 nodes at a time and 1 slow goes 1 node at a time. 
2. Move until we reach a null node or we reach a head pointer
3. if the fast pointer reaches a null node, then there is no cycle
4. if the fast pointer reaches the head pointer, then there is a cycle
5. if the fast pointer reaches the slow pointer, then there is a cycle


Pseudocode...
fast = head.next.next #head??
slow = head.next 
while fast and slow are not null:
  if fast == slow:
    return True
  else: 
    fast = fast.next.next
    slow = slow.next


"""
# Implement
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def hasCycle(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if fast == slow:
      return True
  return False

# Review / Evaluate 
"""
Time complexity: O(n) 
Space complexity: O(1)
"""