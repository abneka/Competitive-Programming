class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        product = 1
        ans = []
        
        for num in nums[::-1]:
            product *= num
            pref.append(product)
        
        product = 1
        pref.pop()
        
        for num in nums:
            ans.append((pref.pop() * product))
            product *= num
        
        return ans
