class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(mid):
            expected_hour = 0
            for i in range(len(piles)):
                if piles[i] <= mid:
                    expected_hour += 1
                else:
                    expected_hour += ceil(piles[i] /mid)
            if expected_hour <= h:
                return True
            else:
                return False

        left = 1
        right = sum(piles)
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            if possible(mid):
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans