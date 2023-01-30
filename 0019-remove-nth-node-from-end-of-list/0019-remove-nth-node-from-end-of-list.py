# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        left = curr = dummy
        curr.next = head
        
        while head:
            if n < 1:
                left = left.next
            head = head.next
            n -= 1
        
        left.next = left.next.next
        return dummy.next 