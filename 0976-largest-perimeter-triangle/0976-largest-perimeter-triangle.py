class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        
        for curr in range(len(nums)-2):
            if nums[curr] + nums[curr+1] > nums[curr+2]: 
                if nums[curr] + nums[curr+2] > nums[curr+1]: 
                    if nums[curr+2] + nums[curr+1] > nums[curr]:
                        return nums[curr] + nums[curr+1] + nums[curr+2]
                    
            
        return 0