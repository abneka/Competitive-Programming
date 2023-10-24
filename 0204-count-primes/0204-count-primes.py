class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [1] * (n+1)

        i = 2
        while i < sqrt(n):
            if nums[i]:
                for j in range(i*2, n, i):
                    nums[j] = 0
            i+=1
        
        return 0 if n < 2 else sum(nums[2:-1])