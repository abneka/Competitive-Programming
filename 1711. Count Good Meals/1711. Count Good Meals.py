class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = {}
        modulus = (10**9) + 7
        
        total = 0
        
        for deli in deliciousness:
            for p in range(22):
                power = (2 ** p) - deli
                
                if power in count:
                    total += count[power]
            
            if not deli in count:
                count[deli] = 0
            count[deli] += 1
        
        return total % modulus
