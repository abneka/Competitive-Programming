# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        stack = []
        res = 0
        while fast and fast.next:
            fast = fast.next.next
            stack.append(slow.val)
            slow = slow.next
            
        for i in range(len(stack)):
            res = max(res, (stack.pop() + slow.val))
            slow = slow.next
        
        return res