class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIp4(ip):
            data = ip.split('.')
            if len(data) == 4:
                for string in data:
                    if not string.isdigit() or str(int(string)) != string:
                        return False
                    if not (0 <= int(string) <= 255):
                        return False
                return True
            return False
        
        def isIp6(ip):
            valid = {"a","b","c","d","e",'f',"A","B","C","D","E","F"}
            array = queryIP.split(":")   

            if len(array) == 8:
                for num in array:
                    if not(1<= len(num) <= 4):
                        return False

                    for char in num:
                        if not char.isdigit() and not char in valid:
                            return False
                return True
            return False
        
        if isIp4(queryIP):
            return 'IPv4'
        
        if isIp6(queryIP):
            return 'IPv6'
        
        return 'Neither'