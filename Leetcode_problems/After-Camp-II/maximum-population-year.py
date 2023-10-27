class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        psum = [0] * 101

        for birth, death in logs:
            psum[birth - 1950] += 1
            psum[death - 1950] -= 1
        
        recent = 0
        maxi = psum[0]

        for year in range(1, len(psum)):
            psum[year] += psum[year - 1]

            if psum[year] > maxi:
                maxi = psum[year]
                recent = year
        
        return recent + 1950