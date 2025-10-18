# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle Edge Case: List has one or two nodes (middle is index 0 or 1)
        # For n=1, middle is 0. For n=2, middle is 1. Deleting it returns the remaining node (or None)
        if head is None or head.next is None:
            return None

        # Create a dummy node to easily handle the case where the middle node is the head
        dummy = ListNode(0, head)
        
        # 'slow' starts at dummy (predecessor of head) to track the node before the middle.
        # 'fast' starts at head.
        slow = dummy
        fast = head

        # The loop condition ensures 'slow' stops right before the middle node.
        # Example: 1->2->3->4 (n=4). Middle index is 2 (node with value 3). Predecessor is node 2.
        # Start: slow=0, fast=1
        # 1st move: slow=1, fast=3
        # 2nd move: fast.next is 4, fast.next.next is None. Loop ends.
        # slow is at node 1 (the predecessor). Correct.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # At this point, slow is the predecessor of the middle node.
        # Delete the middle node by skipping over it.
        # slow.next is the middle node. slow.next.next is the node after the middle.
        slow.next = slow.next.next

        # Return the modified head (which is dummy.next)
        return dummy.next

# Note: The problem defines the middle for n=2 at index 1 (the second node).
# The pointer setup (slow=dummy, fast=head) correctly finds the node *before* index 1.
# List: 1(0) -> 2(1)
# Start: slow=0, fast=1
# Loop ends immediately because fast.next.next is None.
# slow is at node 0 (value 1). slow.next is node 1 (value 2). slow.next.next is None.
# Deletion: slow.next = None. Result: 1. Correct.
