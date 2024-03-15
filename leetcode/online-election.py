class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.lead = defaultdict(int)
        self.time = times
        leader = None
        self.ans = []


        for i in range(len(persons)):
            self.lead[persons[i]] +=1
            if leader == None or self.lead[leader] <= self.lead[persons[i]]:
                leader = persons[i]
            self.ans.append(leader)

            



    def q(self, t: int) -> int:
        
        k = bisect_right(self.time , t) 
        
        return self.ans[k - 1]
         
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)