# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current is not None:
        # 1. Store the next node before breaking the link
        next_node = current.next
        
        # 2. Reverse the link: current node now points backward
        current.next = prev
        
        # 3. Advance pointers one step
        prev = current
        current = next_node

    # 'prev' is the new head (the original tail)
    return prev
