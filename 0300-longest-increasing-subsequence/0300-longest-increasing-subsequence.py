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
        
        '''
        # Bottom up approach
        length = len(nums)
        memo = [1] * length
        ans = 1
        
        for ind, num in enumerate(nums):
            for index in range(ind, -1, -1):
                if nums[index] < num:
                    memo[ind] = max(memo[index] + 1, memo[ind])
                    ans = max(ans, memo[ind])
        
        return ans
        
        '''