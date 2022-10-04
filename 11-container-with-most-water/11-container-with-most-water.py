class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0
        
        while l < r:
            if height[l] > height[r]:
                res = max(res, height[r]*(r-l))
                k = r
                while l < k and height[r] >= height[k]:
                    k -= 1
                r = k
            else:
                res = max(res, height[l]*(r-l))
                k = l
                while k < r and height[k] <= height[l]:
                    k+=1
                l = k
        return res