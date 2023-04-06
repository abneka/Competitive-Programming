class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right):
            pivot = nums[right]
            
            index = left - 1
            
            for i in range(left, right):
                if nums[i] <= pivot:
                    index += 1
                    nums[i], nums[index] = nums[index], nums[i]
                
            nums[index + 1], nums[right] = nums[right], nums[index + 1]
            
            return index + 1
        
        def quickSort(nums, left, right):
            if left < right:
                
                index = partition(nums, left, right)
                
                quickSort(nums, index + 1, right)
                
                quickSort(nums, left, index - 1)
        
        quickSort(nums, 0, len(nums) - 1)
        return nums[-k]