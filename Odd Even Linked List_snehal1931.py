# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases for empty, single, or two-node lists
        if not head or not head.next:
            return head

        # 'odd' starts at the first node (position 1)
        odd = head
        
        # 'even' starts at the second node (position 2)
        even = head.next
        
        # Store the start of the even list to connect it later
        even_head = even 

        # We must continue as long as 'even' has a next node to link to,
        # which guarantees 'odd' also has a next node.
        # The loop condition 'even and even.next' is critical.
        while even and even.next:
            
            # 1. Connect the current ODD node to the NEXT ODD node (skipping the even node)
            # odd.next (node 1) skips the even node (2) and links to the next odd node (3)
            odd.next = even.next
            odd = odd.next  # Move odd pointer forward (to node 3)
            
            # 2. Connect the current EVEN node to the NEXT EVEN node (skipping the odd node)
            # even.next (node 2) skips the odd node (3) and links to the next even node (4)
            even.next = odd.next
            even = even.next # Move even pointer forward (to node 4)
            
        # 3. Final Connection: Append the even list to the tail of the odd list
        odd.next = even_head
        
        return head
