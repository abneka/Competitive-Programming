class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        
        for step in range(2, length):
            cost[step] += min(cost[step - 1], cost[step - 2])
        
        return min(cost[-1], cost[-2])