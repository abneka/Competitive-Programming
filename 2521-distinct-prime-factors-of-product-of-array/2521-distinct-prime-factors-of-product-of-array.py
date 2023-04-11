class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def factorize(val):
            prime = set()
            d = 2
            
            while d*d <= val:
                while val % d == 0:
                    val //= d
                    prime.add(d)
                d += 1
            
            if val > 1:
                prime.add(val)
            return prime
        
        result = set()
        for num in nums:
            result.update(factorize(num))
            
        return len(result)