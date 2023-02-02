# Definition for singly-linked list.
# c/lass ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        counter = 0
        remaining = dummy.next
        nxt = None
        prev = dummy
        
        while remaining:
            counter += 1
            if counter == k:
                
                temp = remaining.next
                remaining.next = None
                remaining = temp
                counter = 0
                
                nxt = prev.next
                prev.next = self.reverseList(nxt)
                nxt.next = remaining
                
                prev = nxt
                continue
                
            remaining = remaining.next
            
        if counter:
            nxt = prev.next
            prev.next = nxt

        return dummy.next
    
    def reverseList(self, head):
        
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
        