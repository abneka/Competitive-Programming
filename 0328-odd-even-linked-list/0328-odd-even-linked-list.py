# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head 
        
        if head is None:
            return head  
        
        right = head.next
        right_head = head.next
        
        while right and right.next:
            left.next = left.next.next
            left = left.next 
            
            right.next = right.next.next 
            right = right.next 
            
        left.next = right_head
        
        return head