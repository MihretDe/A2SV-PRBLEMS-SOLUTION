class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        sum1 = sum(cardPoints[:window_size])
        total_sum = sum(cardPoints)
        left = 0
        right = window_size
        max_sum =total_sum - sum1
        while right < len(cardPoints):
            sum1 -= cardPoints[left]
            sum1 += cardPoints[right]
            left += 1
            right += 1
            max_sum = max(max_sum ,total_sum - sum1)
        return max_sum
        


