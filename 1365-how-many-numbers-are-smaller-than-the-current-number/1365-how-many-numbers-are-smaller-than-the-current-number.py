class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        def default():
            return -1
        
        count = defaultdict(default)
        
        for index, num in enumerate(sorted(nums)):
            if count[num] != -1:
                continue
            count[num] = index
        
        result = []
        # print(count)
        for num in nums:
            result.append(count[num])
        
        return result