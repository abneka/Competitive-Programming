class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for account in accounts:
            maxi = max(maxi, sum(account))
        
        return maxi