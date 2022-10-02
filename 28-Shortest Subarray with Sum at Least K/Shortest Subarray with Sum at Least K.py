class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float('inf')
        queue = deque([[0, 0]])
        total = 0
        
        for index, num in enumerate(nums):
            total += num
            while queue and total - queue[0][0] >= k:
                res = min(res, index + 1 - queue.popleft()[1])
            while queue and total <= queue[-1][0]:
                queue.pop()
            queue.append([total, index + 1])
        
        if res < float('inf'):
            return res
        return -1
    
