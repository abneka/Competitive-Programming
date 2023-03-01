class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        p_sum = [0] * length

        for start, end in requests:
            p_sum[start] += 1
            if end + 1 == length:
                continue
            p_sum[end + 1] -= 1

        prefix = 0
        for index, num in enumerate(p_sum):
            prefix += num
            p_sum[index] = prefix
        

        p_sum.sort()
        nums.sort()

        result = 0

        for num in p_sum[::-1]:
            result += num * nums.pop()


        return result % (10**9 + 7)