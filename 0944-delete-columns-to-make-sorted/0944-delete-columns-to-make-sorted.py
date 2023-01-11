class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        length = len(strs[0])
        ans = 0
        
        for chars in range(length):
            
            for string in range(len(strs)-1):
                
                if ord(strs[string][chars]) > ord(strs[string+1][chars]):
                    ans += 1
                    break
        return ans