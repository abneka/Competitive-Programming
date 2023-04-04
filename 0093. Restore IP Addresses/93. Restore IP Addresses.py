class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)
        if length > 12:
            return []
        ans =  []
        def splitNcheck(index, path):
            if len(path) > 4 or index > length:
                return
            
            if index == length and len(path) == 4:
                print(index, path)
                ans.append('.'.join(path[::]))
                return
            
            string = ''
            for i in range(3):
                if index + i >= length:
                    break
                string += s[index + i]
                if int(string) > 255 or len(string) != len(str(int(string))):
                    break

                path.append(string)
                splitNcheck(index + i + 1, path)
                path.pop()
            
            return
        splitNcheck(0, [])

        return ans
