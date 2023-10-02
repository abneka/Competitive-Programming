class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [float('inf')]
        
        for num in nums:
            index = bisect_left(stack, num)
            
            if index == len(stack):
                stack.append(num)
            else:
                stack[index] = num
        
        return len(stack)