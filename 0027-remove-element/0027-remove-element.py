class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        left = 0
        right = length -1
        occurence = nums.count(val)
        size = length - occurence
        
        while left < size:
            if nums[left] == val:
                while nums[right] == val:
                    right = right - 1
                nums[left] = nums[right]
                right = right -1
            left = left + 1
        
        return size