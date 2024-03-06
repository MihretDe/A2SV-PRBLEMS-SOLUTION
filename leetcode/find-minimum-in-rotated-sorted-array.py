class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = float(inf)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                ans = min (nums[right] , ans)
                left = mid + 1
            else :
                ans = min (nums[left] , ans) 
                ans = min(nums[mid] , ans)
                right = mid - 1
        if left == right:
            ans = min(ans , nums[left])
            ans = min(ans , nums[(left+1) %len(nums)])
            ans = min(ans , nums[(left-1) %len(nums)])
        return ans
            
