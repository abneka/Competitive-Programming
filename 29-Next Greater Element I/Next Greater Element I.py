class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            index = nums2.index(num)
            for great in nums2[index:]:
                if num < great:
                    result.append(great)
                    break
                if great == nums2[-1]:
                    result.append(-1)
        
        return result
