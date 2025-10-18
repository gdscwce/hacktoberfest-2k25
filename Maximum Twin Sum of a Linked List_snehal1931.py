# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Helper function to reverse a linked list
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find the start of the second half using fast/slow pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'slow' is now at the (n/2)-th node, the start of the second half.
        
        # 2. Reverse the second half of the list
        tail = self.reverseList(slow)
        
        # 3. Calculate maximum twin sum
        max_sum = 0
        current_head = head
        current_tail = tail
        
        # Compare nodes from the start of the original list and the reversed second half
        while current_tail:
            current_sum = current_head.val + current_tail.val
            max_sum = max(max_sum, current_sum)
            
            current_head = current_head.next
            current_tail = current_tail.next
            
        return max_sum
