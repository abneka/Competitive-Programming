class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        
        for index, rate in enumerate(rating):
            left_lesser = 0
            right_greater = 0
            left_greater =0 
            right_lesser = 0
            
            for left in rating[:index]:
                if left < rate:
                    left_lesser += 1
                else:
                    left_greater += 1
            
            for right in rating[index + 1:]:
                if right > rate:
                    right_greater += 1
                else:
                    right_lesser += 1
            
            ans += (left_lesser * right_greater) + (left_greater * right_lesser)
            
        return ans
