# Definition for singly-linked list. 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            print("Can't find the LinkedList. It's already empty")
            return

        slow = head
        fast = head
        
        for _ in range(n):
            fast = fast.next

        if fast is None:
            head = head.next
            return head

        # While loop will stop as soon as
        # The fast is None
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
