class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        initial = 0
        ans = 0
        
        for index in range(len(gas)):
            total += gas[index] - cost[index]
            initial += gas[index] - cost[index]
            
            if initial < 0:
                initial = 0
                ans = index + 1
                
        return -1 if total < 0 else ans