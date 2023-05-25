class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        length = len(arr)
        
        for index in range(length - 2, -1, -1):
            if arr[index] > arr[index + 1]:
                for right in range(length -1, index, -1):
                    if arr[right] < arr[index] and arr[right] != arr[right -1]:
                        arr[right], arr[index] = arr[index], arr[right]
                        return arr
        return arr