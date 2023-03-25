class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        kids = [0] * k
        memo = dict()
        def dp(cookie):
            t = tuple(sorted(kids))
            if t in memo: return memo[t]
            if cookie == len(cookies): return max(kids)     
            result = math.inf
            for kid in range(k):
                kids[kid] += cookies[cookie]
                result = min(dp(cookie + 1), result)
                kids[kid] -= cookies[cookie]
            memo[t] = result
            return result                        
        return dp(0)