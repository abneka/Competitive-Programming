class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = Counter()
        
        for index, num in enumerate(nums):
            
            # print(count[num])
            if count[num]:
                # print(count[num], num, index)
                if abs(count[num] - 1 - index) <= k:
                    return True
            
            count[num] = index + 1
            # print(index, count)
        
        return False