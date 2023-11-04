class NumArray:

    def __init__(self, nums: List[int]):
        self.psum = [0]
        for num in nums:
            self.psum.append(self.psum[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right + 1] - self.psum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)