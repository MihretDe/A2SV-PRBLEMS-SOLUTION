class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def possible(mid):
            total = 0
            for i in range(len(nums)):
                total += ceil (nums[i]/mid)
            if total <= threshold:
                return True
            else:
                return False
        
        left = 1
        right = max(nums)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if possible(mid):
                ans = mid
                right = mid -1
                
            else:
                left = mid + 1
        return ans
