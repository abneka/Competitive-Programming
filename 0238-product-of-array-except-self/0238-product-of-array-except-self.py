class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        length = len(nums)
        # res = []
        for i in range(length):
            prefix.append(prefix[-1] * nums[i])
            postfix.insert(0, postfix[0] * nums[length-1-i])
            
        for i in range(length):
            prefix[i] = prefix[i] * postfix[i+1]
        prefix.pop()    
            
        return prefix