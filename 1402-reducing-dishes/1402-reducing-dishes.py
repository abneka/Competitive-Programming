class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        length = len(satisfaction)
        prefix = 0
        ans = 0
        for num in satisfaction:
            prefix += num
            if prefix < 0:
                return ans
            ans += prefix
        return ans