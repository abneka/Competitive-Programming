class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [inf] * n
        prices[src] = 0
        
        for stops in range(k + 1):
            temp = prices.copy()
            for start, end, price in flights:
                if prices[start] == inf:
                    continue
                if prices[start] + price < temp[end]:
                    temp[end] = prices[start] + price
            
            prices = temp
        
        return -1 if prices[dst] == inf else prices[dst]