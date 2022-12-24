class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        curr = 0
        length = len(arr)
        
        for num in arr[:]:
            if not num:
                print('fdf')
                arr[curr] = 0
                curr = curr + 1
                if curr == length:
                    break
                arr[curr] = 0
            else:
                arr[curr] = num
            curr = curr + 1
            if curr == length:
                break
        
        