class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.findBit(n)[k - 1]
        
        
    def findBit(self, n):
        if n == 1:
            return '0'
        
        prev = self.findBit(n - 1)
        
        return prev + '1' + self.rev_invert(prev)
    
    def rev_invert(self, string):
        ans = ''
        
        for char in string[::-1]:
            if char == '1':
                ans += '0'
            
            else:
                ans += '1'
        
        return ans