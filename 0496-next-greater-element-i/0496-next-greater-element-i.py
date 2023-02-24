class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        count = Counter()
        
        for num in nums2:
            while stack and stack[-1] < num:
                count[stack.pop()] = num
            stack.append(num)
            
        for index, num in enumerate(nums1):
            if count[num]:
                nums1[index] = count[num]
            else:
                nums1[index] = -1
        
        return nums1