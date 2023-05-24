class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x: abs(x[0] - x[1]), reverse = True)
        total = 0
        a = b = len(costs) // 2
        
        for city1, city2 in costs:
            if city1 < city2:
                if a:
                    a -= 1
                    total += city1
                else:
                    total += city2
                
            else:
                if b:
                    b -= 1
                    total += city2
                else:
                    total += city1
        
        return total