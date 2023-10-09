class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[-1] * len(nums2) for _ in range(len(nums1))]
        
        def dp(top, bottom):
            if top == len(nums1) or bottom == len(nums2):
                return 0
            
            if memo[top][bottom] == -1:
                if nums1[top] == nums2[bottom]:
                    memo[top][bottom] = 1 + dp(top + 1, bottom + 1)
                    
                else:
                    memo[top][bottom] = max(dp(top + 1, bottom), dp(top, bottom + 1))
            return memo[top][bottom]
        
        return dp(0,0)