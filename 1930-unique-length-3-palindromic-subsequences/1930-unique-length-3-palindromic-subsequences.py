class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = defaultdict(list)
        res = 0
        
        for index, char in enumerate(s):
            if count[char]:
                count[char][1] = index
            
            else:
                count[char].append(index)
                count[char].append(index)
                
        for left, right in count.values():
            if left == right or left == right + 1:
                continue
            
            res += len(set(s[left + 1: right]))
            
        return res