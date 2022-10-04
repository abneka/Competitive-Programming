class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        stack = [num for num in range(1, 1+n)]
        
        while len(stack) != 1:
            stack.pop((i+k-1)%(n))
            i = (i+k-1)%(n)
            n -= 1
            
        return stack[0]
