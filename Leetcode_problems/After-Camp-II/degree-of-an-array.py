class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start = {}
        degree = 0
        ans = 0
        for index, num in enumerate(nums):
            if not num in start:
                start[num] = (0, index)
            start[num] = (start[num][0] + 1, start[num][1])
            if degree < start[num][0]:
                degree = start[num][0]
                ans = (index - start[num][1]) + 1
            elif degree == start[num][0]:
                ans = min(ans, (index - start[num][1]) + 1)
        return ans