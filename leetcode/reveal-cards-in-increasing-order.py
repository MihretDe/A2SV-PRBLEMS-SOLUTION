class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse=True)
        for i in range(len(deck)):
            j = i-1
            current = []
            while j > 0:
                current.append(queue.popleft())
                j -= 1
            queue.appendleft(deck[i])
            for i in range(len(current)):
                queue.append(current[i])
        
        return queue




        
