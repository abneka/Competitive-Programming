class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        length = len(arr)
        
        if length <3:
            return False
        
        maxi = arr[0]
        flag = True
        dec_flag = True
        
        for index in range(1, length):
            
            if arr[index] > maxi and flag:
                maxi = arr[index]
                dec_flag = False
                if index == length -1:
                    return False
                continue
                
            elif arr[index] < maxi:
                flag = False
                maxi = arr[index] 
                if dec_flag:
                    return False
                continue
            
            
            
            return False
        
        return True