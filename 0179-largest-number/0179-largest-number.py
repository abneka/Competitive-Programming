class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a, b):
            return str(a) + str(b) > str(b) + str(a)
        
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))