class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sort = [0] * len(nums)
        ans = []
        for num in nums:
            if sort[num - 1]:
                ans.append(num)
            sort[num - 1] = num
        
        return ans