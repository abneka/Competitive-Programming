class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        length = len(days)
        dp = [float('inf')] * (length + 1)
        dp[-1] = 0
        
        for index in range(length - 1, -1, -1):
            for day, cost in zip([1, 7, 30], costs):
                nextIndex = index
                nextDay = days[index] + day
                
                while nextIndex < length and days[nextIndex] < nextDay:
                    nextIndex += 1
                
                dp[index] = min(dp[index], cost + dp[nextIndex])
        
        return dp[0]
        
#         memo = {}
#         length = len(days)

#         def dp(index):
#             if index == length:
#                 return 0
            
#             if index not in memo:
#                 memo[index] = float('inf')

#                 for day, cost in zip([1, 7, 30], costs):
#                     nextIndex = index
#                     nextDay = days[index] + day

#                     while nextIndex < length and days[nextIndex] < nextDay:
#                         nextIndex += 1

#                     memo[index] = min(memo[index], cost + dp(nextIndex))
            
#             return memo[index]
        
#         return dp(0)