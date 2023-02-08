class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        res = 0
        
        for jewel in jewels:
            res += stones[jewel]
        
        return res