class Solution:
    def fib(self, n: int) -> int:
        
        memo = {}
        
        def fibo(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            if num in memo:
                return memo[num]
            
            memo[num] = (self.fib(num-1) + self.fib(num-2))
            return memo[num]

        return fibo(n)