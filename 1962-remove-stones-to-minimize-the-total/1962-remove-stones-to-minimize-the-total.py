class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = 0
        piles = [-num for num in piles]
        heapify(piles)
        
        while piles:
            num = heappop(piles)
            
            if k:
                heappush(piles, (num//2))
                k -= 1
            
            else:
                total += -num
            
        return total