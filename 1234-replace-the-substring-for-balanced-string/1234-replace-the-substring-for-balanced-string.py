class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        
        res = len(s)
        length = len(s)
        each_count = length // 4 
        
        left = 0
        
        def checkBalance():
            for letter in 'QWER':
                if not each_count >= count[letter]:
                    return False
            
            return True
        
        for index, char in enumerate(s):
            count[char] -= 1
            
            while left < length and checkBalance():
                res = min(res, index - left + 1)
                count[s[left]] += 1
                left += 1
            
        return res