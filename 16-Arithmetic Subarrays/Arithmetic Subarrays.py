class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        sub = []
        for i in range(0, len(l)):
            # for j in range(l[i], r[i]):
            sub = nums[l[i] : r[i]+1]
            sub.sort()
            # print (sub)
            diff = sub[0+1]- sub[0]
            temp = True
            for i in range(1, len(sub)-1):
                if diff != sub[i+1]- sub[i]:
                    temp = False
                    break
            ans.append(temp)
        return ans
                    
                
              
