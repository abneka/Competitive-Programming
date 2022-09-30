class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            k = arr.index(max(arr[:len(arr)-i]))+1
            
            rev = arr[:k]
            rev.reverse()
            arr = rev + arr[k:]
            if k > 1:
                result.append(k)
            
            k = len(arr)-i
            if k > 1:
                result.append(k)
            
            rev = arr[:k]
            rev.reverse()
            arr = rev + arr[k:]
        return result
