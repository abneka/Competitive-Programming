class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxi = -1
        length = len(arr)-1
        
        for index, num in enumerate(arr[::-1][:]):
            arr[length - index] = maxi
            maxi = max(maxi, num)
        
        return arr