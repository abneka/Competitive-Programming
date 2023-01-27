class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        length = len(arr)
        for i in range(length):
            k = arr.index(max(arr[:length - i]))+1
            
            rev = arr[:k]
            rev.reverse()
            arr = rev + arr[k:]
            print(k)
            if k > 1:
                result.append(k)
            
            k = length - i
            if k > 1:
                result.append(k)
            
            rev = arr[:k]
            rev.reverse()
            arr = rev + arr[k:]
            
        return result 