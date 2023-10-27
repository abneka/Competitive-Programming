class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        for index, num in enumerate(nums):
            dic[num].append(index)
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                idx1 = dic[nums[left]][0]
                idx2 = dic[nums[right]][0]
                if idx1 == idx2:
                    idx2 = dic[nums[right]][1]
                return [idx1, idx2]
            
            elif nums[left] + nums[right] < target:
                left += 1

            else:
                right -= 1