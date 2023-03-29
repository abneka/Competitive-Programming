class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for num in range(n + 1):
            # ans.append((bin(num)).count('1'))
            
            index = num
            
            while num:
                if num & 1:
                    ans[index] += 1
                    
                num >>= 1
                        
        return ans