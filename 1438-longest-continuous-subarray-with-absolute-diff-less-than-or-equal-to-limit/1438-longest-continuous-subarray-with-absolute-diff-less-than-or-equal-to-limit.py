class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxi = deque()
        mini = deque()
        res, count = 0, 0
        
        for n in nums:
            while maxi and n > maxi[-1]:
                maxi.pop()
            while mini and n < mini[-1]:
                mini.pop()
            maxi.append(n)
            mini.append(n)
            if maxi[0] - mini[0] > limit:
                if nums[count] == maxi[0]:
                    maxi.popleft()
                if nums[count] == mini[0]:
                    mini.popleft()
                count += 1

        return len(nums)-count
            