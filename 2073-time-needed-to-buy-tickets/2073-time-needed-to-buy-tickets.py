class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        no_of_ticket = tickets[k]
        
        for index, num in enumerate(tickets):
            if index > k:
                total += min(num, no_of_ticket - 1)
                continue
            
            total += min(num, no_of_ticket)
            
        
        return total