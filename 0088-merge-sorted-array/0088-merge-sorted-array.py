class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2[:n]
        # nums1.sort() 
        m_pointer = m + n -1
        
        while nums2:
            if not m:
                nums1[m:m_pointer+1] = nums2[:m_pointer+1]
                break
            if nums1[m-1] < nums2[-1]:
                nums1[m_pointer] = nums2.pop()
                
            else:
                nums1[m_pointer] = nums1[m-1]
                m = m - 1
                
            
            m_pointer = m_pointer - 1
        