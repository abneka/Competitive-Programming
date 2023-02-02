# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        anchor = dummy
        
        
        while anchor:
            if anchor.next and anchor.next.val >= x:
                break
            anchor = anchor.next
        
        
        if not anchor:
            return head


        curr = anchor.next
        
        while curr.next:
            if curr.next.val < x:
                print(curr.next)
                temp = anchor.next
                anchor.next = curr.next
                curr.next = curr.next.next
                anchor = anchor.next
                anchor.next = temp
                continue
                
            curr = curr.next
        
        return dummy.next