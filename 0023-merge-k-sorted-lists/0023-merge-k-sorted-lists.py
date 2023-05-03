# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ans = ListNode()
        curr = ans
        
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index))
        
        while len(heap):
            val, index = heapq.heappop(heap)
            node = lists[index]
            lists[index] = lists[index].next
            curr.next = node
            curr = curr.next
            
            node = node.next
            
            if node:
                heapq.heappush(heap, (node.val, index))
                
        return ans.next
        
        