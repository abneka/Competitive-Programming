class Solution:
    def splitString(self, s: str) -> bool:
        def splitNcheck(string, prev):
            if not string:
                return True
            
            flag = False
            for index in range(len(string)):
                num = int(string[:index + 1])
                
                if prev ==  -1 and int(string) != num:
                    flag = flag or splitNcheck(string[index + 1:], num)
                
                elif num == prev - 1:
                    flag = flag or splitNcheck(string[index + 1:], num)
                    
            return flag
        
        return splitNcheck(s, -1)
