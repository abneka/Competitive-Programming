# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        if head.next == None: 
            return True
        curr = head
        double = head.next
        while double:
            stack.append(curr.val)
            double = double.next
            if double:
                double = double.next
            else:
                break
            curr = curr.next
        curr = curr.next
        while curr:
            if stack[-1] != curr.val:
                return False
            stack.pop()
            curr = curr.next
        return True 