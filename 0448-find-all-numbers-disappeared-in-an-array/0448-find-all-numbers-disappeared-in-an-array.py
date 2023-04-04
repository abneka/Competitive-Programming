class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sort = [0] * len(nums)
        ans = []
        for num in nums:
            sort[num - 1] = num
        
        for index, num in enumerate(sort):
            if not num:
                ans.append(index + 1)
                
        return ans