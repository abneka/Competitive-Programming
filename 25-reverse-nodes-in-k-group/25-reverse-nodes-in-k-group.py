# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseList(h, nu, cont = None):
            prev = cont
            while h and nu:
                nu -= 1
                temp = h.next
                h.next = prev
                prev = h
                h = temp
            return prev
        
        dummy = ListNode()
        curr = dummy
        num = 0
        curr.next = head
        
        while head:
            if num == k-1:
                temp = curr.next
                curr.next = reverseList(curr.next, k, head.next)
                head = temp
                curr = temp
            num = (num +1) % k
            head = head.next
            
        return dummy.next
            
            