class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-num for num in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            
            if x == y:
                continue
            
            heapq.heappush(heap, y - x)
            
        heapq.heappush(heap, 0)
        return -heapq.heappop(heap)