class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        total = 0
        for index, num in enumerate(nums):
            current = num
            
            if current == k:
                total+=1
                
            for ind in range(index + 1,len(nums)):
                current = gcd(current, nums[ind])
                if current == k:
                    total += 1
                
        return total