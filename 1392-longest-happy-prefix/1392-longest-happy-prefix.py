class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        prevLps = 0
        curr = 1
        
        while curr < len(s):
            if s[curr] == s[prevLps]:
                lps[curr] = prevLps + 1
                prevLps += 1
                curr += 1
            
            else:
                if not prevLps:
                    curr += 1
                
                else:
                    prevLps = lps[prevLps - 1]
        
        return s[len(s) - lps[-1]:]