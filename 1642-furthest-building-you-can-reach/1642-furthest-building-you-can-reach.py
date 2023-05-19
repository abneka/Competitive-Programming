class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        length = len(heights) - 1
        
        for i in range(length):
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                heappush(heap,diff)
                
            if len(heap) > ladders:
                bricks -= heappop(heap)
                
            if bricks < 0:
                return i
            
        return length