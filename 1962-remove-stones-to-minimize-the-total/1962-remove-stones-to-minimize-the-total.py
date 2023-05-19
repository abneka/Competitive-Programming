class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [-num for num in piles]
        heapify(piles)
        
        while k and piles:
            num = heappop(piles)
            
            total -= (-num//2)
            num =-( ceil(-num/2))
            
            if num <= -2:
                heappush(piles,num)
            k -= 1
            
        return total