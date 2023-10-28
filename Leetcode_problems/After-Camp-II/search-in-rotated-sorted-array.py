class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        prev = 0
        def find(left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return (True, mid)
                
                elif nums[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1
            return (False, 0)
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                if nums[mid] <= nums[-1]:
                    found, ans = find(mid, right)
                    if found:
                        return ans
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] >= nums[0]:
                    found, ans = find(left, mid)
                    if found:
                        return ans
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1