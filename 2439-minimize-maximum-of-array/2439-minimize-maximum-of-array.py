class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        '''
        [6, 6, 7]
        [3, 7, 9, 6]
         6, 6, 7, 
         3  10 11 17
         3   5  4  5
        '''
        length = len(nums)
        total = sum(nums)
        maxi = max(nums)
        left = total // length
        right = maxi
        ans = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            
            move = 0
            for index in range(length - 1, -1, -1):
                if mid >= nums[index] + move:
                    move = 0
                    continue
                
                move = (nums[index] + move) - mid
            if not move:
                right = mid -1
                ans = min(ans, mid)
                continue
            left = mid + 1
        return ans
            
            
        
        # total = 0
        # ans = float('-inf')
        # for index, num in enumerate(nums, 1):
        #     total += num
        #     ans = max(ans, ceil(total/index))
        #     print(ans)
        # return ans