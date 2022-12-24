class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = 0
        right = length -1
        
        while left < right:
            if nums[left] % 2 != 0:
                while left < right  and nums[right] % 2 != 0:
                    right = right - 1
                nums[left], nums[right] = nums[right], nums[left]
                right = right - 1
            left = left + 1
        
        return nums