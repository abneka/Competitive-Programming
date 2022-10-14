class Solution:
    def canJump(self, nums: List[int]) -> bool:
        print(len(nums))
        maxi = 0
        
        for j, i in enumerate(nums):
            maxi -= 1
            maxi = max(maxi, i)
            print(maxi, i)
            
            if j != len(nums)-1 and not maxi:
                return False
        
        return True