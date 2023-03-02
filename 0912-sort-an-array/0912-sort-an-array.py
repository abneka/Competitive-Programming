class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length < 2:
            return nums
        
        left = 0
        right = length
        mid = right//2
        
        left = self.sortArray(nums[left:mid])
        right = self.sortArray(nums[mid:right])
        return self.merge(left, right)
        
    def merge(self, left, right):
        stack = []
        l = 0
        l_length = len(left)
        r = 0
        r_length = len(right)
        while l < l_length and r < r_length:
            if left[l] > right[r]:
                stack.append(right[r])
                r += 1
                
            else:
                stack.append(left[l])
                l += 1
        
        while r < r_length:
            stack.append(right[r])
            r += 1
        
        while l < l_length:
            stack.append(left[l])
            l += 1
            
        return stack