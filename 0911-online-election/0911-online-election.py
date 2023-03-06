class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = Counter()
        self.persons = persons
        self.times = times
        self.leaders = []
        maxi = 0
        
        for index in range(len(persons)):
            person = persons[index]
            count[person] += 1
            
            if not self.leaders:
                self.leaders.append(person)
                maxi = 1
                
            elif count[person] >= maxi:
                self.leaders.append(person)
                maxi = count[person]
                
            else:
                self.leaders.append(self.leaders[-1])
        
    def q(self, t: int) -> int:
        index = bisect_right(self.times, t) - 1
        return self.leaders[index]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)