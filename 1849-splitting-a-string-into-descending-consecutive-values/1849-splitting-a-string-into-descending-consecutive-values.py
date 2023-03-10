class Solution:
    def splitString(self, s: str) -> bool:
        def splitNcheck(string, prev):
            if not string:
                return True
            
            flag = False
            for index in range(len(string)):
                num = int(string[:index + 1])
                
                if prev ==  -1 and int(string) != num:
                    flag = splitNcheck(string[index + 1:], num) or flag
                
                elif num == prev - 1:
                    flag = splitNcheck(string[index + 1:], num) or flag
                    
            return flag
        
        return splitNcheck(s, -1)
