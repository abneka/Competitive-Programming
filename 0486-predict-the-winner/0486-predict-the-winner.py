class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        def findScore(start, end, pTurn):
            
            if start == end:
                if pTurn:
                    return [nums[start], 0]
                return [0, nums[start]]
            
            option1 = findScore(start + 1, end, not pTurn)
            option2 = findScore(start, end - 1, not pTurn)
            
            if pTurn:
                if option1[0] + nums[start] > option2[0] + nums[end]:
                    option1[0] += nums[start]
                    return option1
                else:
                    option2[0] += nums[end]
                    return option2
            
            if option1[1] + nums[start] > option2[1] + nums[end]:
                option1[1] += nums[start]
                return option1
            else:
                option2[1] += nums[end]
                return option2
            
        # print()
        
        result = findScore(0, len(nums) - 1, True)
        
        if result[0] >= result[1]:
            return True
        
        return False