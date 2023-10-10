class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nee = 0
        curr = 0
        modulo = (10 ** 9) + 7
        
        if len(needle) > len(haystack):
            return -1
        
        def add(num, char):
            num *= 27
            num += (ord(char) - ord('a') + 1)
            num %= modulo
            return num
        
        def remove(num, char):
            num -= ((ord(char) - ord('a') + 1) * (27 ** (len(needle) - 1)))
            return num
        
        for index in range(len(needle)):
            nee = add(nee, needle[index])
            curr = add(curr, haystack[index])
                
        for index in range(len(haystack) - len(needle)):
            if curr == nee:
                return index
            
            curr = remove(curr, haystack[index])
            curr = add(curr, haystack[index + len(needle)])
        
        return -1 if curr != nee else len(haystack) - (len(needle))