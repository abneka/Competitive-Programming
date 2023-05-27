class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        '''
        [6, 6, 7]
        [3, 7, 9, 6]
         6, 6, 7, 
         3  10 11 17
         3   5  4  5
        '''
        total = 0
        ans = float('-inf')
        for index, num in enumerate(nums, 1):
            total += num
            ans = max(ans, ceil(total/index))
        return ans