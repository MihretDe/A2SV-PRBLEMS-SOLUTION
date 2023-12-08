class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set(match[0] for match in matches)
        losers = Counter(match[1] for match in matches)
        lose1_match = [key for key, value in losers.items() if value == 1]
        result = []
        lostno_match = winners - set(losers)
        result.append(sorted(list(lostno_match)))
        result.append(sorted(lose1_match))
        return result
        
    
        
        return result