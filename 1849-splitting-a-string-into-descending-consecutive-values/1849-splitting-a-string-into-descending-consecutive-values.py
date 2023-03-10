class Solution:
    def splitString(self, s: str) -> bool:
        # arr = []
        def splitNcheck(string, prev):
            if not string:
                # print(prev)
                return True
            
            
            flag = False
            # print(string, prev)
            for index in range(len(string)):
                num = int(string[:index + 1])
                
                if prev ==  -1:
                    # print(num)
                    if int(string) == num:
                        break
                    flag = flag or splitNcheck(string[index + 1:], num)
                    # prev = num + 1
                
                if num != prev - 1:
                    # print(num, prev)
                    continue
                
                # prev = num
                flag = flag or splitNcheck(string[index + 1:], num)
            return flag
        
        return splitNcheck(s, -1)
            
        # return False