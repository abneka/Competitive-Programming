class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        
        l = 1
        char = chars[0]
        
        while l < len(chars):
            if char[0] != chars[l]:
                res.append(char[0])
                if len(char) != 1:
                    res.extend(str(len(char))[:]) 
                char = chars[l]
            else:
                char += chars[l]
            l += 1
            
        res.append(char[0])
        if len(char) != 1:
            char = str(len(char))
            res.extend(char[:])
        chars.clear()
        chars.extend(res)