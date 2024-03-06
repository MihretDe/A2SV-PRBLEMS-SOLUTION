class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(mid):
            j = 0
            for i in range(days):
                total = 0
                while j < len(weights ) and total+weights[j] <= mid :
                    total+=weights[j]
                    j+=1
                if j == len(weights):
                    break
            if j < len(weights):
                return False
            else:
                return True
        left = max(weights)
        right = sum(weights)
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            if possible(mid):
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans