class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = 0
        for num in prices:
            while stack and stack[-1] > num:
                ans = max(ans, stack[-1] - stack[0])
                stack.pop()
            stack.append(num)
            
        return max(ans, stack[-1] - stack[0])