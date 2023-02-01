# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        count = 0
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        
        while curr:
            count += 1
            
            if count == left:
                
                right_p = curr.next
                last = curr.next
                
                while right_p and right - left:
                    right_p = right_p.next
                    right -= 1
                
                temp = None
                if right_p:
                    temp = right_p.next
                    right_p.next = None
                    
                curr.next = self.reverseList(curr.next)
                last.next = temp
                break
            curr = curr.next
        
        return dummy.next
    
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev