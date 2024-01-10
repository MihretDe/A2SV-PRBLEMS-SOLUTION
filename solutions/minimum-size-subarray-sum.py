class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        sum1 = 0
        length = float('inf')

        while right < len(nums):
            sum1 += nums[right]
            while sum1 >= target and left < len(nums):
                length = min(length, right - left + 1)
                sum1 -= nums[left]
                left += 1
            right += 1

        return 0 if length == float('inf') else length