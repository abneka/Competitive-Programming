class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        count = Counter()
        
        length = len(s)
        
        left = 0
        ans = [length, [0,0]]
        
        for index, char in enumerate(s):
            
            if t[char]:
                count[char] += 1
            
            while t <= count:
                ans = min(ans, [(index - left), [left, index + 1]])
                
                if t[s[left]]:
                    count[s[left]] -= 1
                
                left += 1
        
        left, right = ans[1]
        
        return s[left : right]