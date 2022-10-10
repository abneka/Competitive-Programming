# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        
        fast = slow.next
        slow.next = None
        slow = fast
        fast = None
        
        while slow:
            temp = slow.next
            slow.next = fast
            fast = slow
            slow = temp
        
        while fast:
            slow = head.next
            head.next = fast
            fast = fast.next
            head.next.next=slow
            head = slow