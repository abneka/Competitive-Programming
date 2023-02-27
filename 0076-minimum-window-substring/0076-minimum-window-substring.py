class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        count = Counter()
        
        length = len(s)
        
        left = 0
        ans = [length, '']
        string = ''
        
        for index, char in enumerate(s):
            string += char
            
            if t[char]:
                count[char] += 1
            
            while t <= count:
                ans = min(ans, [(index - left), string[left:]])
                
                if t[s[left]]:
                    count[s[left]] -= 1
                
                left += 1
        
        return ans[1]