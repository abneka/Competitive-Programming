class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = collections.Counter()
        length = len(nums)
        left, right = 0, 0
        
        while right < length:
            if counter[nums[right]]:
                right += 1
                continue
            
            counter[nums[right]] += 1
            
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right  += 1
            
            
        return left
        
        