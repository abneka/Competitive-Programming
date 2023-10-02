class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pair = [[scores[i] ,ages[i]] for i in range(len(ages))]
        pair.sort()
        memo = [score for score, age in pair]

        for i in range(len(pair)):
            mScore, mAge = pair[i]
            for j in range(i):
                score , age = pair[j]
                if mAge >= age:
                    memo[i] = max(memo[i], mScore + memo[j])
        return max(memo)