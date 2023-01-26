class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distnict = set(nums)
        
        for num in nums:
            string = str(num)
            distnict.add(int(string[::-1]))
        
        return len(distnict)