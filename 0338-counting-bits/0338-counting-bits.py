class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0, 1, 1]
        
        if n <= 2:
            return results[:n+1]
        
        for num in range(3, n+1):
            
            if num % 2:
                results.append(results[-1] + 1)
            else:
                results.append(results[num // 2])
        
        return results