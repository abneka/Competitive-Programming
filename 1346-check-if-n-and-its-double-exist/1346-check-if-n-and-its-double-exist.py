class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for num in arr:
            if num and num*2 in arr:
                return True
            elif not num and arr.count(num) > 1:
                return True
        
        return False