class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = [val for key, val in Counter(nums).items()]
        count.sort(reverse=True)
        fact = [0] * (count[0] + 1)

        for i in range(1, len(fact)):
            fact[i] = (i + fact[i - 1])
        ans = 0

        for c in count:
            ans += fact[c - 1]
        return ans