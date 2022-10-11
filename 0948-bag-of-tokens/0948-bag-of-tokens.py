class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l, r = 0, len(tokens)-1
        tokens.sort()
        res = 0
        while l <= r:
            while l <= r and tokens[l] <= power:
                print(tokens[l])
                power -= tokens[l]
                res += 1
                l += 1
            if not res:
                break
            if res and l < r and tokens[l] > power:
                res -= 1
                power += tokens[r]
            r -= 1
            
        return res