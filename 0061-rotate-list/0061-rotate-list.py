# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        k = k % length
        if k == 0:
            return head
        
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        cur = newhead
        
        for i in range(k - 1):
            cur = cur.next
        cur.next = head
        return newhead
