class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        ans = []
        
        def searchIndex(left, right):
            mini = right + 1
            maxi = left - 1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    mini = searchIndex(left, mid - 1)[0]
                    maxi = searchIndex(mid + 1, right)[1]
                    break
                    
            return [mini, maxi]
                
                
        mini, maxi = searchIndex(low, high)
        
        if mini == -1 or maxi == -1:
            return [-1, -1]
        
        return [mini, maxi]