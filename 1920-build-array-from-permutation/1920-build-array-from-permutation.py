class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        dummy = nums.copy()
        
        for index, num in enumerate(nums[:]):
            
            nums[index] = dummy[num]
            
        return nums