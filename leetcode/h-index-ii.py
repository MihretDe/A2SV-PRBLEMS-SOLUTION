class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = max(citations)
        ans = 0
        while left <= right:
            mid = (left + right ) // 2
            curr = bisect_left(citations , mid)
            if len(citations)  - curr == mid:
                return mid
            elif len(citations)  - curr < mid:
                right = mid -1
            else:
                left = mid + 1
        return right


            
