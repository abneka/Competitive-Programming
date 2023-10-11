class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        
        lps = [0] * len(needle)
        prevLps, index = 0, 1
        
        while index < len(needle):
            if needle[prevLps] == needle[index]:
                lps[index] = prevLps + 1
                prevLps += 1
                index += 1
            
            elif not prevLps:
                lps[index] = 0
                index += 1
            
            else:
                prevLps = lps[prevLps - 1]
        
        i = 0
        j = 0
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            else:
                if not j:
                    i += 1
                else:
                    j = lps[j - 1]
            
            if j == len(needle):
                return i - len(needle)
        return -1
                