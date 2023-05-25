class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: 
            return False
        first = nums[0]
        second = inf
        for curr in nums:
            if curr <= first: 
                first = curr
                
            elif curr < second: 
                second = curr
                
            elif first < second < curr: 
                return True
        return False

        