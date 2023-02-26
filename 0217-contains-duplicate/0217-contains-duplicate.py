class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        return False
    
    
    
    # Solution 2
#         count = Counter()
        
#         for num in nums:
#             if count[num]:
#                 return True
#             count[num] += 1
        
#         return False