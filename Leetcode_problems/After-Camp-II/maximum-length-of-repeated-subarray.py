class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        max_subarray = ''
        nums2 = ''.join([chr(x) for x in nums2])
        ans = 0
        for num in nums1:
            max_subarray += chr(num)
            if max_subarray not in nums2:
                   max_subarray = max_subarray[1:]
            else:
                ans = max(ans ,len(max_subarray))
        return ans  