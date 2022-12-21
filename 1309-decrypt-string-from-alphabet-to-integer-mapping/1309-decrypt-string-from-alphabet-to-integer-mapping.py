class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = [i for i in s]
        chars = {}
        for i in range(ord('a'), ord('z') + 1):
            chars[str(i-96)] = chr(i)
        string = ''
        while s:
            temp = s.pop()
            if temp == '#':
                temp = s.pop()
                temp = s.pop() + temp
            string = string + chars[temp]
                
        return string[::-1]