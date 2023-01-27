class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        left = 0
        right = length -1
        curr = 0
        
        while curr <= right:
            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left +=1
            
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                continue
                
            curr += 1
        
#         while white <=  blue:
#             if nums[white] == 0:
#                 nums[white], nums[red] = nums[red], nums[white]
#                 white += 1
#                 red += 1
            
#             elif nums[white] == 1:
#                 white += 1
            
#             else:
#                 nums[white], nums[blue] = nums[blue], nums[white]
#                 blue -= 1