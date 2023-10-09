class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [0] * (len(nums2) + 1)
        
        for row in range(len(nums1)):
            new = [0] * (len(nums2) + 1)
            for col in range(len(nums2)):
                if nums1[row] == nums2[col]:
                    new[col + 1] = 1 + memo[col]
                
                else:
                    new[col + 1] = max(memo[col + 1], new[col])
            memo = new
        
        return memo[len(nums2)]