class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        counter = set()
        left = 0
        length = float('inf')
        
        for i in range(len(cards)):
            if cards[i] not in counter:
                counter.add(cards[i])
            else:
                while left < i and cards[i] in counter:
                    counter.remove(cards[left])
                    left += 1
                counter.add(cards[i])  
                length = min(length, i - left + 2)
            
        if length == float('inf'):
            return -1
        else:
            return length
