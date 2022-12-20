class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs, key=len)
        for word in strs:
            while short:
                if word.startswith(short):
                    break
                else:
                    short = short[:-1]
            
        return short
                    
            