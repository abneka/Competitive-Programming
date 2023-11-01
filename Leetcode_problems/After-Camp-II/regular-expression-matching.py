class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[-1] * len(p) for _ in range(len(s))]
        def dp(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                if idx1 < 0 and idx2 < 0:
                    return True
                if idx1 < 0 and p[idx2] == '*':
                        return dp(idx1, idx2 - 2)
                return False
            if memo[idx1][idx2] == -1:
                if p[idx2] == '*':
                    if p[idx2 - 1] == '.' or s[idx1] == p[idx2 - 1]:
                        memo[idx1][idx2] = dp(idx1 - 1, idx2) or dp(idx1, idx2 - 2)
                    else:
                        memo[idx1][idx2] = dp(idx1, idx2 - 2)

                elif p[idx2] == s[idx1] or p[idx2] == '.':
                    memo[idx1][idx2] = dp(idx1 - 1, idx2 - 1)
                
                else:
                    memo[idx1][idx2] = False
            return memo[idx1][idx2]
        
        return dp(len(s) - 1, len(p) - 1)
