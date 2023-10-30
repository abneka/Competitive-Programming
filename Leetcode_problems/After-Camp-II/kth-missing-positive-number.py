class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        ans = 0
        for index, num in enumerate(arr):
            print(num - (index + 1))
            if num - (index + 1) >= k:
                return arr[index] + (k - (arr[index] - index))
        return arr[-1] + (k - (arr[-1] - len(arr)))