class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set()
        one = set()
        more = set()

        for win, lose in matches:
            if (win not in one) and (win not in more):
                winner.add(win)
            
            if lose in winner:
                winner.remove(lose)
                one.add(lose)
            elif lose in one:
                one.remove(lose)
                more.add(lose)
            elif lose in more:
                continue
            else:
                one.add(lose)
        
        return [sorted(list(winner)), sorted(list(one))]
