class Solution:
    def canJump(self, nums: List[int]) -> bool:
        print(len(nums))
        maxi = 0
        index = 0
        for i, num in enumerate(nums):
            index = i
            maxi = max(maxi, num)
            if not maxi:
                break
            maxi -= 1
        return index == len(nums)-1