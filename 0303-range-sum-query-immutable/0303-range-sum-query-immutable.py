class NumArray:

    def __init__(self, nums: List[int]):
        self.res = [0]
        for i in nums:
            self.res.append(self.res[-1] + i)
        print(self.res)

    def sumRange(self, left: int, right: int) -> int:
        return self.res[right + 1]-self.res[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)