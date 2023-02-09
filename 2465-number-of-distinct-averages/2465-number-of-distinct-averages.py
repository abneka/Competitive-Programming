class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        distinct = set()
        
        while len(nums) != 0:
            nums = sorted(nums)
            avg = (nums.pop(0) + nums.pop(len(nums)-1))/2
            distinct.add(avg)
            
        return len(distinct)