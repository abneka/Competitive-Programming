class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # 1 4 0 2 0 0
        length = len(nums)
        ans = [0] * length
        num_count = 0
        
        for index in range(length - 1):
            
            if nums[index] == nums[index + 1]:
                nums[index] = nums[index] * 2
                nums[index + 1] = 0
            
            if nums[index] > 0:
                ans[num_count] = nums[index]
                num_count += 1
            
            if nums[index + 1] > 0:
                ans[num_count] = nums[index + 1]
        
        return ans