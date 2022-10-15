class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = [] 
        vacans = [] 
        if len(changed)%2:
                return ans

        changed.sort()

        temp = Counter(changed)
        for i in changed:    
            if temp[i] == 0:  

                continue
            else:
                if temp.get(2*i,0) >= 1:
                    ans.append(i)
                    temp[2*i] -= 1
                    temp[i] -= 1
                else:        
                    return vacans
        return ans