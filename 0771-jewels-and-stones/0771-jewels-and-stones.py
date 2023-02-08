class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = Counter(stones)
        res = 0
        
        for jewel in jewels:
            res += count[jewel]
        
        return res