class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        mod=len(piles)//3
        total=0
        for i in range(1,len(piles)-mod,2):
            total += piles[i]
        return total
