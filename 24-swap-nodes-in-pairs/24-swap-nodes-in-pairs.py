# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        prev = head
        if head:
            curr = head.next
            if head.next: 
                head = curr
        while curr:
            prev.next = curr.next
            curr.next = prev
            if prev.next and prev.next.next:
                temp = prev.next
                curr = prev.next.next
                prev.next = curr
                prev = temp
            else:
                break
        return head