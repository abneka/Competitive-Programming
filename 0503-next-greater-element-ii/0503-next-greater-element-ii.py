class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        
        result = [-1] * len(nums)
        
        for _ in range(2):
            for index in range(len(nums)):
                
                while stack and nums[stack[-1]] < nums[index]:
                    result[stack.pop()] = nums[index]
                
                stack.append(index)
        
        return result